from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
    # Unit Testing SetUp 
    def setUp(self):
        Post.objects.create(idpost = 1,
                            title = "My Test Blog #1", 
                            content = "<p>Django’s unit tests use a Python standard library module:" + 
                                        "<a class='reference external' href='https://docs.python.org/3/library/unittest.html#module-unittest' title='(in Python v3.7)'>" +
                                            "<code class='xref py py-mod docutils literal notranslate'>" +
                                                "<span class='pre'>unittest</span>" +
                                            "</code>" +
                                        "</a>" + 
                                        ". Thismodule defines tests using a class-based approach." + 
                                    "</p>",
                            textcontent = "Django’s unit tests use a Python standard library module: unittest. Thismodule defines tests using a class-based approach. ",
                            author = "Rafael García Cuéllar", 
                            section = "Unit Testing Django",
                            tags = "'Django','Unit','Testing'",
                            image = "pexels-photo-733872.jpeg",
                            date = "2018-10-09")

    # Validate Output Tags - Test 
    def test_validate_tags(self):
        post = Post.objects.get(idpost = 1)
        tagsExpected = ['Django', 'Unit', 'Testing']
        tagsResponse = post.tags_as_list()
        self.assertEqual(tagsResponse, tagsExpected)

    # Image extension validation - Test
    def test_image_extension(self):
        post = Post.objects.get(idpost = 1)
        extensions = ['.tif', '.tiff', '.gif', '.jpeg', '.jpg', '.jif', '.jfif', '.jp2', '.jpx', '.j2k', '.j2c', '.fpx', '.pcd', '.png', '.psd', '.pdf', '.svg', '.raw', '.nef', '.ai']
        imageString = str(post.image)
        fileExtension = imageString[imageString.find('.'):len(imageString)]
        self.assertIn(fileExtension, extensions)

        """  Addmit Extension by Pillow - https://pillow.readthedocs.io/en/5.3.x/handbook/image-file-formats.html 
            .bmp	Mapa de bits
            .gif	Imagen en movimiento
            .jpg	Joint Photographic Experts Group
            .png	Portable Network Graphics
            .psd	Photoshop
            .ai	    Adobe illustrator
            .cdr	Corel Draw
            .dwg	AutoCAD
            .svg	Scalable Vector Graphics
            .raw	imagen RAW, directa del sensor de una cámara digital, negativo digital.
            .nef	imagen RAW tomada por una cámara Nikon 1​
        """

    # Validate Date with Regex Expression - Test
    def test_date_validator(self):
        post = Post.objects.get(idpost = 1);
        #                                               yyyy-mm-dd
        self.assertRegex(str(post.date), r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))")
