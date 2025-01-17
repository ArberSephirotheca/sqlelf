# Without this Python was complaining
from __future__ import annotations

from typing import Any, Iterator

import apsw
import apsw.ext
import capstone
import lief


def elf_instructions(binaries: list[lief.Binary]):
    def generator() -> Iterator[dict[str, Any]]:
        for binary in binaries:
            for section in binary.sections:
                if section.has(lief.ELF.SECTION_FLAGS.EXECINSTR):
                    data = bytes(section.content)
                    md = capstone.Cs(arch(binary), mode(binary))
                    # keep in mind that producing details costs more memory,
                    # complicates the internal operations and slows down
                    # the engine a bit, so only do that if needed.
                    md.detail = False
                    for (address, size, mnemonic, op_str) in md.disasm_lite(
                        data, section.virtual_address
                    ):
                        yield {
                            "path": binary.name,
                            "section": section.name,
                            "mnemonic": mnemonic,
                            "address": address,
                            "operands": op_str,
                        }

    return generator


def mode(binary: lief.Binary) -> int:
    if binary.header.identity_class == lief.ELF.ELF_CLASS.CLASS64:
        return capstone.CS_MODE_64
    raise Exception(f"Unknown mode for {binary.name}")


def arch(binary: lief.Binary) -> int:
    if binary.header.machine_type == lief.ELF.ARCH.x86_64:
        return capstone.CS_ARCH_X86
    raise Exception(f"Unknown machine type for {binary.name}")


def register(connection: apsw.Connection, binaries: list[lief.Binary]):
    generator = elf_instructions(binaries)
    # setup columns and access by providing an example of the first entry returned
    generator.columns, generator.column_access = apsw.ext.get_column_names(
        next(generator())
    )
    apsw.ext.make_virtual_module(connection, "elf_instructions", generator)
