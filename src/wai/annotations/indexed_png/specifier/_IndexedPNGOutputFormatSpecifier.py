from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SinkStageSpecifier


class IndexedPNGOutputFormatSpecifier(SinkStageSpecifier):
    """
    Specifier of the components for writing indexed-PNG format
    image-segmentation annotations.
    """
    @classmethod
    def description(cls) -> str:
        return "Writes image segmentation files in the indexed-PNG format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ..component import ToIndexedPNG, IndexedPNGWriter
        return ToIndexedPNG, IndexedPNGWriter

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.segmentation import ImageSegmentationDomainSpecifier
        return ImageSegmentationDomainSpecifier
