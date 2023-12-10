# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrganizationOrganizationItemRead(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'name': 'str',
        'streetno': 'str',
        'zip': 'str',
        'city': 'str',
        'country': 'str',
        'note': 'str',
        'settings': 'str',
        'task_sets': 'list[str]',
        'task_step_categories': 'list[str]',
        'form_sets': 'list[str]',
        'licenses': 'list[str]',
        'groups': 'list[str]',
        'parent_organization_settings': 'list[str]',
        'users': 'list[str]',
        'privacies': 'list[str]',
        'terms_of_use': 'list[str]',
        'logo': 'AnyOfOrganizationOrganizationItemReadLogo',
        'former_users': 'list[str]',
        'blok_id': 'int',
        'e_cademy_token': 'str',
        'scorms': 'list[str]',
        'jobs': 'list[str]',
        'equipment': 'list[str]',
        'background_file': 'AnyOfOrganizationOrganizationItemReadBackgroundFile',
        'christiani_ids': 'list[str]',
        'scorm_groups': 'list[str]',
        'equipment_locations': 'list[str]',
        'app_tags': 'list[str]',
        'organization_head_file': 'AnyOfOrganizationOrganizationItemReadOrganizationHeadFile',
        'organization_footer_file': 'AnyOfOrganizationOrganizationItemReadOrganizationFooterFile',
        'organization_header_file': 'AnyOfOrganizationOrganizationItemReadOrganizationHeaderFile',
        'shared_task_sets': 'list[str]',
        'user_invitations': 'list[str]',
        'organization_in_group': 'str',
        'autofachmann_subscription_no': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'name': 'name',
        'streetno': 'streetno',
        'zip': 'zip',
        'city': 'city',
        'country': 'country',
        'note': 'note',
        'settings': 'settings',
        'task_sets': 'taskSets',
        'task_step_categories': 'taskStepCategories',
        'form_sets': 'formSets',
        'licenses': 'licenses',
        'groups': 'groups',
        'parent_organization_settings': 'parentOrganizationSettings',
        'users': 'users',
        'privacies': 'privacies',
        'terms_of_use': 'termsOfUse',
        'logo': 'logo',
        'former_users': 'formerUsers',
        'blok_id': 'blokId',
        'e_cademy_token': 'eCademyToken',
        'scorms': 'scorms',
        'jobs': 'jobs',
        'equipment': 'equipment',
        'background_file': 'backgroundFile',
        'christiani_ids': 'christianiIds',
        'scorm_groups': 'scormGroups',
        'equipment_locations': 'equipmentLocations',
        'app_tags': 'appTags',
        'organization_head_file': 'organizationHeadFile',
        'organization_footer_file': 'organizationFooterFile',
        'organization_header_file': 'organizationHeaderFile',
        'shared_task_sets': 'sharedTaskSets',
        'user_invitations': 'userInvitations',
        'organization_in_group': 'organizationInGroup',
        'autofachmann_subscription_no': 'autofachmannSubscriptionNo'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, name=None, streetno=None, zip=None, city=None, country=None, note=None, settings=None, task_sets=None, task_step_categories=None, form_sets=None, licenses=None, groups=None, parent_organization_settings=None, users=None, privacies=None, terms_of_use=None, logo=None, former_users=None, blok_id=None, e_cademy_token=None, scorms=None, jobs=None, equipment=None, background_file=None, christiani_ids=None, scorm_groups=None, equipment_locations=None, app_tags=None, organization_head_file=None, organization_footer_file=None, organization_header_file=None, shared_task_sets=None, user_invitations=None, organization_in_group=None, autofachmann_subscription_no=None):  # noqa: E501
        """OrganizationOrganizationItemRead - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._name = None
        self._streetno = None
        self._zip = None
        self._city = None
        self._country = None
        self._note = None
        self._settings = None
        self._task_sets = None
        self._task_step_categories = None
        self._form_sets = None
        self._licenses = None
        self._groups = None
        self._parent_organization_settings = None
        self._users = None
        self._privacies = None
        self._terms_of_use = None
        self._logo = None
        self._former_users = None
        self._blok_id = None
        self._e_cademy_token = None
        self._scorms = None
        self._jobs = None
        self._equipment = None
        self._background_file = None
        self._christiani_ids = None
        self._scorm_groups = None
        self._equipment_locations = None
        self._app_tags = None
        self._organization_head_file = None
        self._organization_footer_file = None
        self._organization_header_file = None
        self._shared_task_sets = None
        self._user_invitations = None
        self._organization_in_group = None
        self._autofachmann_subscription_no = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        self.name = name
        self.streetno = streetno
        self.zip = zip
        self.city = city
        self.country = country
        if note is not None:
            self.note = note
        if settings is not None:
            self.settings = settings
        if task_sets is not None:
            self.task_sets = task_sets
        if task_step_categories is not None:
            self.task_step_categories = task_step_categories
        if form_sets is not None:
            self.form_sets = form_sets
        if licenses is not None:
            self.licenses = licenses
        if groups is not None:
            self.groups = groups
        if parent_organization_settings is not None:
            self.parent_organization_settings = parent_organization_settings
        if users is not None:
            self.users = users
        if privacies is not None:
            self.privacies = privacies
        if terms_of_use is not None:
            self.terms_of_use = terms_of_use
        if logo is not None:
            self.logo = logo
        if former_users is not None:
            self.former_users = former_users
        if blok_id is not None:
            self.blok_id = blok_id
        if e_cademy_token is not None:
            self.e_cademy_token = e_cademy_token
        if scorms is not None:
            self.scorms = scorms
        if jobs is not None:
            self.jobs = jobs
        if equipment is not None:
            self.equipment = equipment
        if background_file is not None:
            self.background_file = background_file
        if christiani_ids is not None:
            self.christiani_ids = christiani_ids
        if scorm_groups is not None:
            self.scorm_groups = scorm_groups
        if equipment_locations is not None:
            self.equipment_locations = equipment_locations
        if app_tags is not None:
            self.app_tags = app_tags
        if organization_head_file is not None:
            self.organization_head_file = organization_head_file
        if organization_footer_file is not None:
            self.organization_footer_file = organization_footer_file
        if organization_header_file is not None:
            self.organization_header_file = organization_header_file
        if shared_task_sets is not None:
            self.shared_task_sets = shared_task_sets
        if user_invitations is not None:
            self.user_invitations = user_invitations
        if organization_in_group is not None:
            self.organization_in_group = organization_in_group
        if autofachmann_subscription_no is not None:
            self.autofachmann_subscription_no = autofachmann_subscription_no

    @property
    def created_at(self):
        """Gets the created_at of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The created_at of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrganizationOrganizationItemRead.


        :param created_at: The created_at of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The updated_at of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OrganizationOrganizationItemRead.


        :param updated_at: The updated_at of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The id of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationOrganizationItemRead.


        :param id: The id of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The name of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationOrganizationItemRead.


        :param name: The name of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def streetno(self):
        """Gets the streetno of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The streetno of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._streetno

    @streetno.setter
    def streetno(self, streetno):
        """Sets the streetno of this OrganizationOrganizationItemRead.


        :param streetno: The streetno of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """
        if streetno is None:
            raise ValueError("Invalid value for `streetno`, must not be `None`")  # noqa: E501

        self._streetno = streetno

    @property
    def zip(self):
        """Gets the zip of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The zip of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this OrganizationOrganizationItemRead.


        :param zip: The zip of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def city(self):
        """Gets the city of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The city of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrganizationOrganizationItemRead.


        :param city: The city of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def country(self):
        """Gets the country of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The country of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrganizationOrganizationItemRead.


        :param country: The country of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def note(self):
        """Gets the note of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The note of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this OrganizationOrganizationItemRead.


        :param note: The note of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def settings(self):
        """Gets the settings of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The settings of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this OrganizationOrganizationItemRead.


        :param settings: The settings of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """

        self._settings = settings

    @property
    def task_sets(self):
        """Gets the task_sets of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The task_sets of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_sets

    @task_sets.setter
    def task_sets(self, task_sets):
        """Sets the task_sets of this OrganizationOrganizationItemRead.


        :param task_sets: The task_sets of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._task_sets = task_sets

    @property
    def task_step_categories(self):
        """Gets the task_step_categories of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The task_step_categories of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_step_categories

    @task_step_categories.setter
    def task_step_categories(self, task_step_categories):
        """Sets the task_step_categories of this OrganizationOrganizationItemRead.


        :param task_step_categories: The task_step_categories of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._task_step_categories = task_step_categories

    @property
    def form_sets(self):
        """Gets the form_sets of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The form_sets of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_sets

    @form_sets.setter
    def form_sets(self, form_sets):
        """Sets the form_sets of this OrganizationOrganizationItemRead.


        :param form_sets: The form_sets of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._form_sets = form_sets

    @property
    def licenses(self):
        """Gets the licenses of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The licenses of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this OrganizationOrganizationItemRead.


        :param licenses: The licenses of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._licenses = licenses

    @property
    def groups(self):
        """Gets the groups of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The groups of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OrganizationOrganizationItemRead.


        :param groups: The groups of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def parent_organization_settings(self):
        """Gets the parent_organization_settings of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The parent_organization_settings of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_organization_settings

    @parent_organization_settings.setter
    def parent_organization_settings(self, parent_organization_settings):
        """Sets the parent_organization_settings of this OrganizationOrganizationItemRead.


        :param parent_organization_settings: The parent_organization_settings of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._parent_organization_settings = parent_organization_settings

    @property
    def users(self):
        """Gets the users of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The users of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this OrganizationOrganizationItemRead.


        :param users: The users of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def privacies(self):
        """Gets the privacies of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The privacies of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._privacies

    @privacies.setter
    def privacies(self, privacies):
        """Sets the privacies of this OrganizationOrganizationItemRead.


        :param privacies: The privacies of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._privacies = privacies

    @property
    def terms_of_use(self):
        """Gets the terms_of_use of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The terms_of_use of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms_of_use

    @terms_of_use.setter
    def terms_of_use(self, terms_of_use):
        """Sets the terms_of_use of this OrganizationOrganizationItemRead.


        :param terms_of_use: The terms_of_use of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._terms_of_use = terms_of_use

    @property
    def logo(self):
        """Gets the logo of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The logo of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: AnyOfOrganizationOrganizationItemReadLogo
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this OrganizationOrganizationItemRead.


        :param logo: The logo of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: AnyOfOrganizationOrganizationItemReadLogo
        """

        self._logo = logo

    @property
    def former_users(self):
        """Gets the former_users of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The former_users of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._former_users

    @former_users.setter
    def former_users(self, former_users):
        """Sets the former_users of this OrganizationOrganizationItemRead.


        :param former_users: The former_users of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._former_users = former_users

    @property
    def blok_id(self):
        """Gets the blok_id of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The blok_id of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: int
        """
        return self._blok_id

    @blok_id.setter
    def blok_id(self, blok_id):
        """Sets the blok_id of this OrganizationOrganizationItemRead.


        :param blok_id: The blok_id of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: int
        """

        self._blok_id = blok_id

    @property
    def e_cademy_token(self):
        """Gets the e_cademy_token of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The e_cademy_token of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._e_cademy_token

    @e_cademy_token.setter
    def e_cademy_token(self, e_cademy_token):
        """Sets the e_cademy_token of this OrganizationOrganizationItemRead.


        :param e_cademy_token: The e_cademy_token of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """

        self._e_cademy_token = e_cademy_token

    @property
    def scorms(self):
        """Gets the scorms of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The scorms of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._scorms

    @scorms.setter
    def scorms(self, scorms):
        """Sets the scorms of this OrganizationOrganizationItemRead.


        :param scorms: The scorms of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._scorms = scorms

    @property
    def jobs(self):
        """Gets the jobs of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The jobs of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this OrganizationOrganizationItemRead.


        :param jobs: The jobs of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._jobs = jobs

    @property
    def equipment(self):
        """Gets the equipment of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The equipment of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this OrganizationOrganizationItemRead.


        :param equipment: The equipment of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._equipment = equipment

    @property
    def background_file(self):
        """Gets the background_file of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The background_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: AnyOfOrganizationOrganizationItemReadBackgroundFile
        """
        return self._background_file

    @background_file.setter
    def background_file(self, background_file):
        """Sets the background_file of this OrganizationOrganizationItemRead.


        :param background_file: The background_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: AnyOfOrganizationOrganizationItemReadBackgroundFile
        """

        self._background_file = background_file

    @property
    def christiani_ids(self):
        """Gets the christiani_ids of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The christiani_ids of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._christiani_ids

    @christiani_ids.setter
    def christiani_ids(self, christiani_ids):
        """Sets the christiani_ids of this OrganizationOrganizationItemRead.


        :param christiani_ids: The christiani_ids of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._christiani_ids = christiani_ids

    @property
    def scorm_groups(self):
        """Gets the scorm_groups of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The scorm_groups of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._scorm_groups

    @scorm_groups.setter
    def scorm_groups(self, scorm_groups):
        """Sets the scorm_groups of this OrganizationOrganizationItemRead.


        :param scorm_groups: The scorm_groups of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._scorm_groups = scorm_groups

    @property
    def equipment_locations(self):
        """Gets the equipment_locations of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The equipment_locations of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment_locations

    @equipment_locations.setter
    def equipment_locations(self, equipment_locations):
        """Sets the equipment_locations of this OrganizationOrganizationItemRead.


        :param equipment_locations: The equipment_locations of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._equipment_locations = equipment_locations

    @property
    def app_tags(self):
        """Gets the app_tags of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The app_tags of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_tags

    @app_tags.setter
    def app_tags(self, app_tags):
        """Sets the app_tags of this OrganizationOrganizationItemRead.


        :param app_tags: The app_tags of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._app_tags = app_tags

    @property
    def organization_head_file(self):
        """Gets the organization_head_file of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The organization_head_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: AnyOfOrganizationOrganizationItemReadOrganizationHeadFile
        """
        return self._organization_head_file

    @organization_head_file.setter
    def organization_head_file(self, organization_head_file):
        """Sets the organization_head_file of this OrganizationOrganizationItemRead.


        :param organization_head_file: The organization_head_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: AnyOfOrganizationOrganizationItemReadOrganizationHeadFile
        """

        self._organization_head_file = organization_head_file

    @property
    def organization_footer_file(self):
        """Gets the organization_footer_file of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The organization_footer_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: AnyOfOrganizationOrganizationItemReadOrganizationFooterFile
        """
        return self._organization_footer_file

    @organization_footer_file.setter
    def organization_footer_file(self, organization_footer_file):
        """Sets the organization_footer_file of this OrganizationOrganizationItemRead.


        :param organization_footer_file: The organization_footer_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: AnyOfOrganizationOrganizationItemReadOrganizationFooterFile
        """

        self._organization_footer_file = organization_footer_file

    @property
    def organization_header_file(self):
        """Gets the organization_header_file of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The organization_header_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: AnyOfOrganizationOrganizationItemReadOrganizationHeaderFile
        """
        return self._organization_header_file

    @organization_header_file.setter
    def organization_header_file(self, organization_header_file):
        """Sets the organization_header_file of this OrganizationOrganizationItemRead.


        :param organization_header_file: The organization_header_file of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: AnyOfOrganizationOrganizationItemReadOrganizationHeaderFile
        """

        self._organization_header_file = organization_header_file

    @property
    def shared_task_sets(self):
        """Gets the shared_task_sets of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The shared_task_sets of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_task_sets

    @shared_task_sets.setter
    def shared_task_sets(self, shared_task_sets):
        """Sets the shared_task_sets of this OrganizationOrganizationItemRead.


        :param shared_task_sets: The shared_task_sets of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_task_sets = shared_task_sets

    @property
    def user_invitations(self):
        """Gets the user_invitations of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The user_invitations of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_invitations

    @user_invitations.setter
    def user_invitations(self, user_invitations):
        """Sets the user_invitations of this OrganizationOrganizationItemRead.


        :param user_invitations: The user_invitations of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._user_invitations = user_invitations

    @property
    def organization_in_group(self):
        """Gets the organization_in_group of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The organization_in_group of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._organization_in_group

    @organization_in_group.setter
    def organization_in_group(self, organization_in_group):
        """Sets the organization_in_group of this OrganizationOrganizationItemRead.


        :param organization_in_group: The organization_in_group of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """

        self._organization_in_group = organization_in_group

    @property
    def autofachmann_subscription_no(self):
        """Gets the autofachmann_subscription_no of this OrganizationOrganizationItemRead.  # noqa: E501


        :return: The autofachmann_subscription_no of this OrganizationOrganizationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._autofachmann_subscription_no

    @autofachmann_subscription_no.setter
    def autofachmann_subscription_no(self, autofachmann_subscription_no):
        """Sets the autofachmann_subscription_no of this OrganizationOrganizationItemRead.


        :param autofachmann_subscription_no: The autofachmann_subscription_no of this OrganizationOrganizationItemRead.  # noqa: E501
        :type: str
        """

        self._autofachmann_subscription_no = autofachmann_subscription_no

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrganizationOrganizationItemRead, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrganizationOrganizationItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
