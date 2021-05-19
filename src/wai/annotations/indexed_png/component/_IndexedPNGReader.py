import os
from PIL import Image as PILImage

from wai.annotations.core.component.util import AnnotationFileProcessor
from wai.annotations.core.stream import ThenFunction
from wai.annotations.domain.image import Image, ImageFormat
from wai.annotations.domain.image.segmentation.util import RelativeDataPathMixin
from ..util import IndexedPNGFormat


class IndexedPNGReader(
    RelativeDataPathMixin,
    AnnotationFileProcessor[IndexedPNGFormat]
):
    """
    Reader of image-segmentation data-sets which store annotations
    in an indexed PNG image.
    """
    def read_annotation_file(self, filename: str, then: ThenFunction[IndexedPNGFormat]):
        # Get the associated data image
        data_image_filename = self.get_associated_image(
            filename,
            [ImageFormat.JPG, ImageFormat.BMP, ImageFormat.PNG]
        )

        # If the data image found was the annotations image, throw an error
        if data_image_filename is None or os.path.normpath(data_image_filename) == os.path.normpath(filename):
            raise Exception(f"Couldn't find data-image associated with {filename}")

        then(
            IndexedPNGFormat(
                Image.from_file(data_image_filename),
                PILImage.open(filename)
            )
        )

    def read_negative_file(self, filename: str, then: ThenFunction[IndexedPNGFormat]):
        then(
            IndexedPNGFormat(
                Image.from_file(filename),
                None
            )
        )
