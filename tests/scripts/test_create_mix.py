"""Tests for ``siptools.scripts.create_mix`` module"""
import siptools.scripts.create_mix


def test_inspect_image():
    """Test for ``_inspect_image`` function. Pass a sample image file for
    function and check that expected metada is found.
    """

    # pylint: disable=protected-access
    metadata = siptools.scripts.create_mix._inspect_image(
        'tests/data/images/tiff1.tif'
    )

    assert metadata["compression"] == 'b44a'
    assert metadata["byteorder"] == "little endian"
    assert metadata["width"] == "2"
    assert metadata["height"] == "2"
    assert metadata["colorspace"] == "srgb"
    assert metadata["bitspersample"] == "8"
    assert metadata["bpsunit"] == "integer"
    assert metadata["samplesperpixel"] == "3"


def test_create_mix():
    """Test ``_create_mix`` function. Pass valid metadata dictionary to
    function and check that result XML element contains expected elements.
    """
    metadata = {"compression": "foo",
                "byteorder": "foo",
                "width": "foo",
                "height": "foo",
                "colorspace": "foo",
                "bitspersample": "1",
                "bpsunit": "foo",
                "samplesperpixel": "foo"}

    # pylint: disable=protected-access
    xml = siptools.scripts.create_mix._create_mix(metadata)
    namespaces = {'ns0': "http://www.loc.gov/mix/v20"}

    # compression
    xpath = '/ns0:mix/ns0:BasicDigitalObjectInformation/ns0:Compression/'\
        'ns0:compressionScheme'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"

    # byteorder
    xpath = '/ns0:mix/ns0:BasicDigitalObjectInformation/ns0:byteOrder'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"

    # width
    xpath = '/ns0:mix/ns0:BasicImageInformation/'\
        'ns0:BasicImageCharacteristics/ns0:imageWidth'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"

    # height
    xpath = '/ns0:mix/ns0:BasicImageInformation/'\
            'ns0:BasicImageCharacteristics/ns0:imageHeight'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"

    # colorspace
    xpath = '/ns0:mix/ns0:BasicImageInformation/'\
            'ns0:BasicImageCharacteristics/ns0:PhotometricInterpretation/'\
            'ns0:colorSpace'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"

    # bitspresample
    xpath = '/ns0:mix/ns0:ImageAssessmentMetadata/ns0:ImageColorEncoding/'\
            'ns0:BitsPerSample/ns0:bitsPerSampleValue'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "1"

    # bpsunit
    xpath = '/ns0:mix/ns0:ImageAssessmentMetadata/ns0:ImageColorEncoding/'\
            'ns0:BitsPerSample/ns0:bitsPerSampleUnit'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"

    # samplesperpixel
    xpath = '/ns0:mix/ns0:ImageAssessmentMetadata/ns0:ImageColorEncoding/'\
            'ns0:samplesPerPixel'
    assert xml.xpath(xpath, namespaces=namespaces)[0].text == "foo"