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

class OrganizationJsonldOrganizationWrite(object):
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
        'context': 'OneOfOrganizationJsonldOrganizationWriteContext',
        'id': 'str',
        'type': 'str',
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
        'groups': 'list[str]',
        'users': 'list[str]',
        'privacies': 'list[str]',
        'terms_of_use': 'list[str]',
        'logo': 'str',
        'mls1_id': 'int',
        'former_users': 'list[str]',
        'jobs': 'list[str]',
        'equipment': 'list[str]',
        'background_file': 'str',
        'scorm_groups': 'list[str]',
        'equipment_locations': 'list[str]',
        'app_tags': 'list[str]',
        'organization_head_file': 'str',
        'organization_footer_file': 'str',
        'organization_header_file': 'str',
        'shared_task_sets': 'list[str]',
        'user_invitations': 'list[str]',
        'organization_in_group': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
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
        'groups': 'groups',
        'users': 'users',
        'privacies': 'privacies',
        'terms_of_use': 'termsOfUse',
        'logo': 'logo',
        'mls1_id': 'mls1Id',
        'former_users': 'formerUsers',
        'jobs': 'jobs',
        'equipment': 'equipment',
        'background_file': 'backgroundFile',
        'scorm_groups': 'scormGroups',
        'equipment_locations': 'equipmentLocations',
        'app_tags': 'appTags',
        'organization_head_file': 'organizationHeadFile',
        'organization_footer_file': 'organizationFooterFile',
        'organization_header_file': 'organizationHeaderFile',
        'shared_task_sets': 'sharedTaskSets',
        'user_invitations': 'userInvitations',
        'organization_in_group': 'organizationInGroup'
    }

    def __init__(self, context=None, id=None, type=None, name=None, streetno=None, zip=None, city=None, country=None, note=None, settings=None, task_sets=None, task_step_categories=None, form_sets=None, groups=None, users=None, privacies=None, terms_of_use=None, logo=None, mls1_id=None, former_users=None, jobs=None, equipment=None, background_file=None, scorm_groups=None, equipment_locations=None, app_tags=None, organization_head_file=None, organization_footer_file=None, organization_header_file=None, shared_task_sets=None, user_invitations=None, organization_in_group=None):  # noqa: E501
        """OrganizationJsonldOrganizationWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
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
        self._groups = None
        self._users = None
        self._privacies = None
        self._terms_of_use = None
        self._logo = None
        self._mls1_id = None
        self._former_users = None
        self._jobs = None
        self._equipment = None
        self._background_file = None
        self._scorm_groups = None
        self._equipment_locations = None
        self._app_tags = None
        self._organization_head_file = None
        self._organization_footer_file = None
        self._organization_header_file = None
        self._shared_task_sets = None
        self._user_invitations = None
        self._organization_in_group = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
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
        if groups is not None:
            self.groups = groups
        if users is not None:
            self.users = users
        if privacies is not None:
            self.privacies = privacies
        if terms_of_use is not None:
            self.terms_of_use = terms_of_use
        if logo is not None:
            self.logo = logo
        if mls1_id is not None:
            self.mls1_id = mls1_id
        if former_users is not None:
            self.former_users = former_users
        if jobs is not None:
            self.jobs = jobs
        if equipment is not None:
            self.equipment = equipment
        if background_file is not None:
            self.background_file = background_file
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

    @property
    def context(self):
        """Gets the context of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The context of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: OneOfOrganizationJsonldOrganizationWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this OrganizationJsonldOrganizationWrite.


        :param context: The context of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: OneOfOrganizationJsonldOrganizationWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The id of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationJsonldOrganizationWrite.


        :param id: The id of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The type of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrganizationJsonldOrganizationWrite.


        :param type: The type of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The name of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationJsonldOrganizationWrite.


        :param name: The name of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def streetno(self):
        """Gets the streetno of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The streetno of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._streetno

    @streetno.setter
    def streetno(self, streetno):
        """Sets the streetno of this OrganizationJsonldOrganizationWrite.


        :param streetno: The streetno of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """
        if streetno is None:
            raise ValueError("Invalid value for `streetno`, must not be `None`")  # noqa: E501

        self._streetno = streetno

    @property
    def zip(self):
        """Gets the zip of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The zip of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this OrganizationJsonldOrganizationWrite.


        :param zip: The zip of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def city(self):
        """Gets the city of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The city of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrganizationJsonldOrganizationWrite.


        :param city: The city of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def country(self):
        """Gets the country of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The country of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrganizationJsonldOrganizationWrite.


        :param country: The country of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def note(self):
        """Gets the note of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The note of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this OrganizationJsonldOrganizationWrite.


        :param note: The note of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def settings(self):
        """Gets the settings of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The settings of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this OrganizationJsonldOrganizationWrite.


        :param settings: The settings of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._settings = settings

    @property
    def task_sets(self):
        """Gets the task_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The task_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_sets

    @task_sets.setter
    def task_sets(self, task_sets):
        """Sets the task_sets of this OrganizationJsonldOrganizationWrite.


        :param task_sets: The task_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_sets = task_sets

    @property
    def task_step_categories(self):
        """Gets the task_step_categories of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The task_step_categories of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_step_categories

    @task_step_categories.setter
    def task_step_categories(self, task_step_categories):
        """Sets the task_step_categories of this OrganizationJsonldOrganizationWrite.


        :param task_step_categories: The task_step_categories of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_step_categories = task_step_categories

    @property
    def form_sets(self):
        """Gets the form_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The form_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_sets

    @form_sets.setter
    def form_sets(self, form_sets):
        """Sets the form_sets of this OrganizationJsonldOrganizationWrite.


        :param form_sets: The form_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._form_sets = form_sets

    @property
    def groups(self):
        """Gets the groups of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The groups of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OrganizationJsonldOrganizationWrite.


        :param groups: The groups of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def users(self):
        """Gets the users of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The users of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this OrganizationJsonldOrganizationWrite.


        :param users: The users of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def privacies(self):
        """Gets the privacies of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The privacies of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._privacies

    @privacies.setter
    def privacies(self, privacies):
        """Sets the privacies of this OrganizationJsonldOrganizationWrite.


        :param privacies: The privacies of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._privacies = privacies

    @property
    def terms_of_use(self):
        """Gets the terms_of_use of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The terms_of_use of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms_of_use

    @terms_of_use.setter
    def terms_of_use(self, terms_of_use):
        """Sets the terms_of_use of this OrganizationJsonldOrganizationWrite.


        :param terms_of_use: The terms_of_use of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._terms_of_use = terms_of_use

    @property
    def logo(self):
        """Gets the logo of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The logo of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this OrganizationJsonldOrganizationWrite.


        :param logo: The logo of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def mls1_id(self):
        """Gets the mls1_id of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The mls1_id of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this OrganizationJsonldOrganizationWrite.


        :param mls1_id: The mls1_id of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: int
        """

        self._mls1_id = mls1_id

    @property
    def former_users(self):
        """Gets the former_users of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The former_users of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._former_users

    @former_users.setter
    def former_users(self, former_users):
        """Sets the former_users of this OrganizationJsonldOrganizationWrite.


        :param former_users: The former_users of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._former_users = former_users

    @property
    def jobs(self):
        """Gets the jobs of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The jobs of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this OrganizationJsonldOrganizationWrite.


        :param jobs: The jobs of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._jobs = jobs

    @property
    def equipment(self):
        """Gets the equipment of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The equipment of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this OrganizationJsonldOrganizationWrite.


        :param equipment: The equipment of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._equipment = equipment

    @property
    def background_file(self):
        """Gets the background_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The background_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._background_file

    @background_file.setter
    def background_file(self, background_file):
        """Sets the background_file of this OrganizationJsonldOrganizationWrite.


        :param background_file: The background_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._background_file = background_file

    @property
    def scorm_groups(self):
        """Gets the scorm_groups of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The scorm_groups of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._scorm_groups

    @scorm_groups.setter
    def scorm_groups(self, scorm_groups):
        """Sets the scorm_groups of this OrganizationJsonldOrganizationWrite.


        :param scorm_groups: The scorm_groups of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._scorm_groups = scorm_groups

    @property
    def equipment_locations(self):
        """Gets the equipment_locations of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The equipment_locations of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment_locations

    @equipment_locations.setter
    def equipment_locations(self, equipment_locations):
        """Sets the equipment_locations of this OrganizationJsonldOrganizationWrite.


        :param equipment_locations: The equipment_locations of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._equipment_locations = equipment_locations

    @property
    def app_tags(self):
        """Gets the app_tags of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The app_tags of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_tags

    @app_tags.setter
    def app_tags(self, app_tags):
        """Sets the app_tags of this OrganizationJsonldOrganizationWrite.


        :param app_tags: The app_tags of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._app_tags = app_tags

    @property
    def organization_head_file(self):
        """Gets the organization_head_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The organization_head_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization_head_file

    @organization_head_file.setter
    def organization_head_file(self, organization_head_file):
        """Sets the organization_head_file of this OrganizationJsonldOrganizationWrite.


        :param organization_head_file: The organization_head_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._organization_head_file = organization_head_file

    @property
    def organization_footer_file(self):
        """Gets the organization_footer_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The organization_footer_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization_footer_file

    @organization_footer_file.setter
    def organization_footer_file(self, organization_footer_file):
        """Sets the organization_footer_file of this OrganizationJsonldOrganizationWrite.


        :param organization_footer_file: The organization_footer_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._organization_footer_file = organization_footer_file

    @property
    def organization_header_file(self):
        """Gets the organization_header_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The organization_header_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization_header_file

    @organization_header_file.setter
    def organization_header_file(self, organization_header_file):
        """Sets the organization_header_file of this OrganizationJsonldOrganizationWrite.


        :param organization_header_file: The organization_header_file of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._organization_header_file = organization_header_file

    @property
    def shared_task_sets(self):
        """Gets the shared_task_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The shared_task_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_task_sets

    @shared_task_sets.setter
    def shared_task_sets(self, shared_task_sets):
        """Sets the shared_task_sets of this OrganizationJsonldOrganizationWrite.


        :param shared_task_sets: The shared_task_sets of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._shared_task_sets = shared_task_sets

    @property
    def user_invitations(self):
        """Gets the user_invitations of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The user_invitations of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_invitations

    @user_invitations.setter
    def user_invitations(self, user_invitations):
        """Sets the user_invitations of this OrganizationJsonldOrganizationWrite.


        :param user_invitations: The user_invitations of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: list[str]
        """

        self._user_invitations = user_invitations

    @property
    def organization_in_group(self):
        """Gets the organization_in_group of this OrganizationJsonldOrganizationWrite.  # noqa: E501


        :return: The organization_in_group of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization_in_group

    @organization_in_group.setter
    def organization_in_group(self, organization_in_group):
        """Sets the organization_in_group of this OrganizationJsonldOrganizationWrite.


        :param organization_in_group: The organization_in_group of this OrganizationJsonldOrganizationWrite.  # noqa: E501
        :type: str
        """

        self._organization_in_group = organization_in_group

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
        if issubclass(OrganizationJsonldOrganizationWrite, dict):
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
        if not isinstance(other, OrganizationJsonldOrganizationWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
