from django.db import models


class Aboutus(models.Model):
    words = models.TextField(blank=True, null=True, verbose_name='Words (separated by comma)')

    # Camion - Delivery
    icon1_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 1 - Title')
    icon1_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Icono 1 - Description')

    # Reloj - Time
    icon2_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 2 - Title')
    icon2_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Icono 2 - Description')

    # Corazon - Passion
    icon3_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 3 - Title')
    icon3_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Icono 3 - Description')

    # Maleta - Professional
    icon4_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 4 - Title')
    icon4_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Icono 4 - Description')

    def __str__(self):
        return "About US"

    class Meta:
        verbose_name = 'ABOUT US'
        verbose_name_plural = 'ABOUT US'
        db_table = 'aboutus'

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.words = self.words.upper()
        super(Aboutus, self).save(force_insert, force_update, using)


class Services(models.Model):
    header1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 1')
    header2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 2')

    # Service 1
    icon1_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 1')
    icon1_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description 1')
    icon1_image = models.FileField(upload_to='services/', max_length=100, blank=True, null=True)

    # Service 2
    icon2_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 2')
    icon2_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description 2')
    icon2_image = models.FileField(upload_to='services/', max_length=100, blank=True, null=True)

    # Service 3
    icon3_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 3')
    icon3_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description 3')
    icon3_image = models.FileField(upload_to='services/', max_length=100, blank=True, null=True)

    def __str__(self):
        return "Services"

    class Meta:
        verbose_name = 'SERVICES'
        verbose_name_plural = 'SERVICES'
        db_table = 'services'

    def download_icon1_image(self):
        if self.icon1_image:
            return self.icon1_image.url
        return ''

    def download_icon2_image(self):
        if self.icon2_image:
            return self.icon2_image.url
        return ''

    def download_icon3_image(self):
        if self.icon3_image:
            return self.icon3_image.url
        return ''

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.icon1_title = self.icon1_title.upper()
        self.icon2_title = self.icon2_title.upper()
        self.icon3_title = self.icon3_title.upper()
        super(Services, self).save(force_insert, force_update, using)


class Whyus(models.Model):
    header1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 1')
    header2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 2')
    avatar = models.FileField(upload_to='avatars/', max_length=100, blank=True, null=True)

    # Camion - Delivery
    icon1_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 1 - Title')
    icon1_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Icono 1 - Description')

    # Reloj - Time
    icon2_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 2 - Title')
    icon2_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Icono 2 - Description')

    # Corazon - Passion
    icon3_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 3 - Title')
    icon3_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Icono 3 - Description')

    # Maleta - Professional
    icon4_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Icono 4 - Title')
    icon4_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Icono 4 - Description')

    def __str__(self):
        return "Why Choose Us"

    class Meta:
        verbose_name = 'WHY CHOOSE US'
        verbose_name_plural = 'WHY CHOOSE US'
        db_table = 'whyus'

    def download_avatar(self):
        if self.avatar:
            return self.avatar.url
        return ''


class Projects(models.Model):
    header1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 1')
    header2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 2')

    # Project 1
    icon1_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 1')
    icon1_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon1_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 2
    icon2_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 2')
    icon2_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon2_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 3
    icon3_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 3')
    icon3_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon3_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 4
    icon4_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 4')
    icon4_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon4_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 5
    icon5_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 5')
    icon5_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon5_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 6
    icon6_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 6')
    icon6_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon6_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 7
    icon7_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 7')
    icon7_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon7_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Project 8
    icon8_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Title 8')
    icon8_image = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)
    icon8_image_big = models.FileField(upload_to='projects/', max_length=100, blank=True, null=True)

    # Numbers Section
    number_1 = models.IntegerField(default=0)
    title_number1 = models.CharField(max_length=50, blank=True, null=True)

    number_2 = models.IntegerField(default=0)
    title_number2 = models.CharField(max_length=50, blank=True, null=True)

    number_3 = models.IntegerField(default=0)
    title_number3 = models.CharField(max_length=50, blank=True, null=True)

    number_4 = models.IntegerField(default=0)
    title_number4 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Projects"

    class Meta:
        verbose_name = 'PROJECTS'
        verbose_name_plural = 'PROJECTS'
        db_table = 'projects'

    def download_icon1_image(self):
        if self.icon1_image:
            return self.icon1_image.url
        return ''

    def download_icon1_image_big(self):
        if self.icon1_image_big:
            return self.icon1_image_big.url
        return ''

    def download_icon2_image(self):
        if self.icon2_image:
            return self.icon2_image.url
        return ''

    def download_icon2_image_big(self):
        if self.icon2_image_big:
            return self.icon2_image_big.url
        return ''

    def download_icon3_image(self):
        if self.icon3_image:
            return self.icon3_image.url
        return ''

    def download_icon3_image_big(self):
        if self.icon3_image_big:
            return self.icon3_image_big.url
        return ''

    def download_icon4_image(self):
        if self.icon4_image:
            return self.icon4_image.url
        return ''

    def download_icon4_image_big(self):
        if self.icon4_image_big:
            return self.icon4_image_big.url
        return ''

    def download_icon5_image(self):
        if self.icon5_image:
            return self.icon5_image.url
        return ''

    def download_icon5_image_big(self):
        if self.icon5_image_big:
            return self.icon5_image_big.url
        return ''

    def download_icon6_image(self):
        if self.icon6_image:
            return self.icon6_image.url
        return ''

    def download_icon6_image_big(self):
        if self.icon6_image_big:
            return self.icon6_image_big.url
        return ''

    def download_icon7_image(self):
        if self.icon7_image:
            return self.icon7_image.url
        return ''

    def download_icon7_image_big(self):
        if self.icon7_image_big:
            return self.icon7_image_big.url
        return ''

    def download_icon8_image(self):
        if self.icon8_image:
            return self.icon8_image.url
        return ''

    def download_icon8_image_big(self):
        if self.icon8_image_big:
            return self.icon8_image_big.url
        return ''

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.icon1_title = self.icon1_title.upper()
        self.icon2_title = self.icon2_title.upper()
        self.icon3_title = self.icon3_title.upper()
        self.icon4_title = self.icon4_title.upper()
        self.icon5_title = self.icon5_title.upper()
        self.icon6_title = self.icon6_title.upper()
        self.icon7_title = self.icon7_title.upper()
        self.icon8_title = self.icon8_title.upper()
        self.title_number1 = self.title_number1.upper()
        self.title_number2 = self.title_number2.upper()
        self.title_number3 = self.title_number3.upper()
        self.title_number4 = self.title_number4.upper()
        super(Projects, self).save(force_insert, force_update, using)


class Team(models.Model):
    header1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 1')
    header2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 2')

    # Team 1
    icon1_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name - Team 1')
    icon1_position = models.CharField(max_length=50, blank=True, null=True, verbose_name='Position - Team 1')
    icon1_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description - Team 1')
    icon1_image = models.FileField(upload_to='teams/', max_length=100, null=True, verbose_name='Image - Team 1')
    icon1_facebook = models.CharField(max_length=300, blank=True, null=True, verbose_name='Facebook URL - Team 1')
    icon1_twitter = models.CharField(max_length=300, blank=True, null=True, verbose_name='Twitter URL - Team 1')
    icon1_linkedin = models.CharField(max_length=300, blank=True, null=True, verbose_name='Linkedin URL - Team 1')

    # Team 2
    icon2_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name - Team 2')
    icon2_position = models.CharField(max_length=50, blank=True, null=True, verbose_name='Position - Team 2')
    icon2_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description - Team 2')
    icon2_image = models.FileField(upload_to='teams/', max_length=100, null=True, verbose_name='Image - Team 2')
    icon2_facebook = models.CharField(max_length=300, blank=True, null=True, verbose_name='Facebook URL - Team 2')
    icon2_twitter = models.CharField(max_length=300, blank=True, null=True, verbose_name='Twitter URL - Team 2')
    icon2_linkedin = models.CharField(max_length=300, blank=True, null=True, verbose_name='Linkedin URL - Team 2')

    # Team 3
    icon3_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name - Team 3')
    icon3_position = models.CharField(max_length=50, blank=True, null=True, verbose_name='Position - Team 3')
    icon3_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description - Team 3')
    icon3_image = models.FileField(upload_to='teams/', max_length=100, null=True, verbose_name='Image - Team 3')
    icon3_facebook = models.CharField(max_length=300, blank=True, null=True, verbose_name='Facebook URL - Team 3')
    icon3_twitter = models.CharField(max_length=300, blank=True, null=True, verbose_name='Twitter URL - Team 3')
    icon3_linkedin = models.CharField(max_length=300, blank=True, null=True, verbose_name='Linkedin URL - Team 3')

    # Team 4
    icon4_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name - Team 4')
    icon4_position = models.CharField(max_length=50, blank=True, null=True, verbose_name='Position - Team 4')
    icon4_description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description - Team 4')
    icon4_image = models.FileField(upload_to='teams/', max_length=100, null=True, verbose_name='Image - Team 4')
    icon4_facebook = models.CharField(max_length=300, blank=True, null=True, verbose_name='Facebook URL - Team 4')
    icon4_twitter = models.CharField(max_length=300, blank=True, null=True, verbose_name='Twitter URL - Team 4')
    icon4_linkedin = models.CharField(max_length=300, blank=True, null=True, verbose_name='Linkedin URL - Team 4')

    def __str__(self):
        return "Team"

    class Meta:
        verbose_name = 'TEAM'
        verbose_name_plural = 'TEAM'
        db_table = 'team'

    def download_icon1_image(self):
        if self.icon1_image:
            return self.icon1_image.url
        return ''

    def download_icon2_image(self):
        if self.icon2_image:
            return self.icon2_image.url
        return ''

    def download_icon3_image(self):
        if self.icon3_image:
            return self.icon3_image.url
        return ''

    def download_icon4_image(self):
        if self.icon4_image:
            return self.icon4_image.url
        return ''


class Newsletter(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Newsletter Email')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return "Newsletters"

    class Meta:
        verbose_name = 'NEWSLETTER'
        verbose_name_plural = 'NEWSLETTERS'
        db_table = 'newsletters'


class Clients(models.Model):
    header1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 1')
    header2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 2')

    # Client 1
    icon1_image = models.FileField(upload_to='clients/', max_length=100, blank=True, null=True,
                                   verbose_name='Image - Client 1')
    icon1_url = models.CharField(max_length=300, blank=True, null=True, verbose_name='URL - Client 1')

    # Client 2
    icon2_image = models.FileField(upload_to='clients/', max_length=100, blank=True, null=True,
                                   verbose_name='Image - Client 2')
    icon2_url = models.CharField(max_length=300, blank=True, null=True, verbose_name='URL - Client 2')

    # Client 3
    icon3_image = models.FileField(upload_to='clients/', max_length=100, blank=True, null=True,
                                   verbose_name='Image - Client 3')
    icon3_url = models.CharField(max_length=300, blank=True, null=True, verbose_name='URL - Client 3')

    # Client 4
    icon4_image = models.FileField(upload_to='clients/', max_length=100, blank=True, null=True,
                                   verbose_name='Image - Client 4')
    icon4_url = models.CharField(max_length=300, blank=True, null=True, verbose_name='URL - Client 4')

    def __str__(self):
        return "Clients"

    class Meta:
        verbose_name = 'CLIENT'
        verbose_name_plural = 'CLIENTS'
        db_table = 'clients'

    def download_icon1_image(self):
        if self.icon1_image:
            return self.icon1_image.url
        return ''

    def download_icon2_image(self):
        if self.icon2_image:
            return self.icon2_image.url
        return ''

    def download_icon3_image(self):
        if self.icon3_image:
            return self.icon3_image.url
        return ''

    def download_icon4_image(self):
        if self.icon4_image:
            return self.icon4_image.url
        return ''


CONTACT_TYPES = (
    (1, 'MARKETING'),
    (2, 'SALES'),
    (3, 'PARTNERSHIP'),
    (4, 'PRICE ENQUIRY'),
    (5, 'OTHER'),
)


class Contacts(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Last Name')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Email')
    contact_type = models.IntegerField(choices=CONTACT_TYPES, default=1, verbose_name='Contact Type')
    message = models.TextField(blank=True, null=True, verbose_name='Message')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Contacts"

    class Meta:
        verbose_name = 'CONTACT'
        verbose_name_plural = 'CONTACTS'
        db_table = 'contacts'

    def get_contact_type_name(self):
        if self.contact_type == 1:
            return 'MARKETING'
        elif self.contact_type == 2:
            return 'SALES'
        elif self.contact_type == 3:
            return 'PARTNERSHIP'
        elif self.contact_type == 4:
            return 'PRICE ENQUIRY'
        else:
            return 'OTHER'


class Company(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name='Name')
    email = models.CharField(max_length=200, blank=True, null=True, verbose_name='Email')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='Address')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Phone')

    # Social Networks
    facebook = models.CharField(max_length=300, blank=True, null=True, verbose_name='Facebook')
    twitter = models.CharField(max_length=300, blank=True, null=True, verbose_name='Twitter')
    youtube = models.CharField(max_length=300, blank=True, null=True, verbose_name='Youtube')
    instagram = models.CharField(max_length=300, blank=True, null=True, verbose_name='Instagram')
    pinterest = models.CharField(max_length=300, blank=True, null=True, verbose_name='Pinterest')
    google = models.CharField(max_length=300, blank=True, null=True, verbose_name='Google+')
    linkedin = models.CharField(max_length=300, blank=True, null=True, verbose_name='LinkedIn')

    def __str__(self):
        return "Company"

    class Meta:
        verbose_name = 'COMPANY'
        verbose_name_plural = 'COMPANY'
        db_table = 'company'


class Construction(models.Model):
    header1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 1')
    header2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Header 2')
    header_image = models.FileField(upload_to='constructions/', max_length=100, blank=True, null=True, verbose_name='Header Image')

    # Construction little images slide
    image1 = models.FileField(upload_to='constructions/', max_length=100, blank=True, null=True, verbose_name='Image 1')
    image2 = models.FileField(upload_to='constructions/', max_length=100, blank=True, null=True, verbose_name='Image 2')
    image3 = models.FileField(upload_to='constructions/', max_length=100, blank=True, null=True, verbose_name='Image 3')

    subservices = models.TextField(blank=True, null=True, verbose_name='Services (separated by semicolon)')

    # Concept 1
    concept_title_1 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Concept Title 1')
    concept_description_1 = models.TextField(blank=True, null=True, verbose_name='Concept Description 1')

    # Concept 2
    concept_title_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Concept Title 2')
    concept_description_2 = models.TextField(blank=True, null=True, verbose_name='Concept Description 2')

    # Concept 3
    concept_title_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Concept Title 3')
    concept_description_3 = models.TextField(blank=True, null=True, verbose_name='Concept Description 3')

    # Concept 4
    concept_title_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Concept Title 4')
    concept_description_4 = models.TextField(blank=True, null=True, verbose_name='Concept Description 4')

    def __str__(self):
        return "Service - Construction"

    class Meta:
        verbose_name = 'SERVICE - CONSTRUCTION'
        verbose_name_plural = 'SERVICES - CONSTRUCTION'
        db_table = 'construction'

    def download_header_image(self):
        if self.header_image:
            return self.header_image.url
        return ''

    def download_image1(self):
        if self.image1:
            return self.image1.url
        return ''

    def download_image2(self):
        if self.image2:
            return self.image2.url
        return ''

    def download_image3(self):
        if self.image3:
            return self.image3.url
        return ''

    def get_services_list(self):
        return self.subservices.split(';')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.header1 = self.header1.upper()
        self.header2 = self.header2.upper()
        self.concept_title_1 = self.concept_title_1.upper()
        self.concept_title_2 = self.concept_title_2.upper()
        self.concept_title_3 = self.concept_title_3.upper()
        self.concept_title_4 = self.concept_title_4.upper()
        super(Construction, self).save(force_insert, force_update, using)
