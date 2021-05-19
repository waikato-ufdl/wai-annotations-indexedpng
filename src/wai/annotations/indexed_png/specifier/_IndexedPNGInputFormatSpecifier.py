from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SourceStageSpecifier


class IndexedPNGInputFormatSpecifier(SourceStageSpecifier):
    """
    Specifier of the components for reading indexed-PNG format
    image-segmentation annotations.
    """
    @classmethod
    def description(cls) -> str:
        return "Reads image segmentation files in the indexed-PNG format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from wai.annotations.core.component.util import LocalFilenameSource
        from ..component import IndexedPNGReader, FromIndexedPNG
        return LocalFilenameSource, IndexedPNGReader, FromIndexedPNG

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.segmentation import ImageSegmentationDomainSpecifier
        return ImageSegmentationDomainSpecifier
