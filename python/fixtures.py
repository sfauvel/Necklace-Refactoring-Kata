import pytest

from jewellery_storage import JewelleryStorage, Jewellery, Necklace, Earring, PendantNecklace
from packer import pack_necklace


@pytest.fixture
def jewellery_storage():
    return JewelleryStorage()


def print_jewellery(item: Jewellery):
    if isinstance(item, PendantNecklace):
        return f"{print_jewellery(item.chain)} with pendant {print_jewellery(item.pendant)}"
    elif isinstance(item, (Earring, Necklace)):
        return f"{item.type.name} {item.__class__.__name__} of {item.stone.name}"
    else:
        return f"{item.__class__.__name__} of {item.stone.name}"

def print_jewellery_storage(storage: JewelleryStorage):
    contents = f"""\
Jewellery Storage:

[%autowidth]
|====
.3+| Box | Ring Compartment |   {storage.box.ring_compartment}
| Top Shelf |                   {storage.box.top_shelf}
| Main Section |                {storage.box.main_section}
2+| Tree |                      {storage.tree}
2+| Travel Roll |               {storage.travel_roll}
2+| Safe |                      {storage.safe}
2+| On top of dresser |         {storage.dresser_top}
|====
"""
    return contents