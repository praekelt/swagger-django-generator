import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import {
    InvitationList,
    InvitationCreate,
    InvitationShow,
    InvitationEdit,
} from './Invitation';

import {
    SiteList,
    SiteCreate,
    SiteShow,
    SiteEdit,
} from './Site';

import {
    InvitationSiteRoleList,
    InvitationSiteRoleShow,
    InvitationSiteRoleCreate,
} from './InvitationSiteRole';

import {
    ResourceList,
    ResourceCreate,
    ResourceShow,
    ResourceEdit,
} from './Resource';

import {
    ClientList,
    ClientShow,
} from './Client';

import {
    DomainRoleList,
    DomainRoleCreate,
    DomainRoleShow,
    DomainRoleEdit,
} from './DomainRole';

import {
    DomainShow,
    DomainEdit,
    DomainCreate,
    DomainList,
} from './Domain';

import {
    RoleResourcePermissionList,
    RoleResourcePermissionShow,
    RoleResourcePermissionCreate,
} from './RoleResourcePermission';

import {
    SiteRoleShow,
    SiteRoleEdit,
    SiteRoleCreate,
    SiteRoleList,
} from './SiteRole';

import {
    InvitationDomainRoleList,
    InvitationDomainRoleShow,
    InvitationDomainRoleCreate,
} from './InvitationDomainRole';

import {
    UserSiteDataList,
    UserSiteDataCreate,
    UserSiteDataShow,
    UserSiteDataEdit,
} from './UserSiteData';

import {
    RoleList,
    RoleCreate,
    RoleShow,
    RoleEdit,
} from './Role';

import {
    AdminNoteShow,
    AdminNoteEdit,
    AdminNoteCreate,
    AdminNoteList,
} from './AdminNote';

import {
    SiteDataSchemaShow,
    SiteDataSchemaEdit,
    SiteDataSchemaCreate,
    SiteDataSchemaList,
} from './SiteDataSchema';

import {
    UserList,
    UserShow,
    UserEdit,
} from './User';

import {
    PermissionShow,
    PermissionEdit,
    PermissionCreate,
    PermissionList,
} from './Permission';

import {
    UserDomainRoleShow,
    UserDomainRoleCreate,
    UserDomainRoleList,
} from './UserDomainRole';

import {
    UserSiteRoleShow,
    UserSiteRoleCreate,
    UserSiteRoleList,
} from './UserSiteRole';



const App = () => (
    <Admin title={"ManagementLayer"} restClient={simpleRestClient}>
        <Resource
            name="invitations"
            list={ InvitationList }
            create={ InvitationCreate }
            show={ InvitationShow }
            edit={ InvitationEdit }
            remove={Delete}
        />
        <Resource
            name="sites"
            list={ SiteList }
            create={ SiteCreate }
            show={ SiteShow }
            edit={ SiteEdit }
            remove={Delete}
        />
        <Resource
            name="invitationsiteroles"
            list={ InvitationSiteRoleList }
            show={ InvitationSiteRoleShow }
            create={ InvitationSiteRoleCreate }
            remove={Delete}
        />
        <Resource
            name="resources"
            list={ ResourceList }
            create={ ResourceCreate }
            show={ ResourceShow }
            edit={ ResourceEdit }
            remove={Delete}
        />
        <Resource
            name="clients"
            list={ ClientList }
            show={ ClientShow }
            remove={Delete}
        />
        <Resource
            name="domainroles"
            list={ DomainRoleList }
            create={ DomainRoleCreate }
            show={ DomainRoleShow }
            edit={ DomainRoleEdit }
            remove={Delete}
        />
        <Resource
            name="domains"
            show={ DomainShow }
            edit={ DomainEdit }
            create={ DomainCreate }
            list={ DomainList }
            remove={Delete}
        />
        <Resource
            name="roleresourcepermissions"
            list={ RoleResourcePermissionList }
            show={ RoleResourcePermissionShow }
            create={ RoleResourcePermissionCreate }
            remove={Delete}
        />
        <Resource
            name="siteroles"
            show={ SiteRoleShow }
            edit={ SiteRoleEdit }
            create={ SiteRoleCreate }
            list={ SiteRoleList }
            remove={Delete}
        />
        <Resource
            name="invitationdomainroles"
            list={ InvitationDomainRoleList }
            show={ InvitationDomainRoleShow }
            create={ InvitationDomainRoleCreate }
            remove={Delete}
        />
        <Resource
            name="usersitedata"
            list={ UserSiteDataList }
            create={ UserSiteDataCreate }
            show={ UserSiteDataShow }
            edit={ UserSiteDataEdit }
            remove={Delete}
        />
        <Resource
            name="roles"
            list={ RoleList }
            create={ RoleCreate }
            show={ RoleShow }
            edit={ RoleEdit }
            remove={Delete}
        />
        <Resource
            name="adminnotes"
            show={ AdminNoteShow }
            edit={ AdminNoteEdit }
            create={ AdminNoteCreate }
            list={ AdminNoteList }
            remove={Delete}
        />
        <Resource
            name="sitedataschemas"
            show={ SiteDataSchemaShow }
            edit={ SiteDataSchemaEdit }
            create={ SiteDataSchemaCreate }
            list={ SiteDataSchemaList }
            remove={Delete}
        />
        <Resource
            name="users"
            list={ UserList }
            show={ UserShow }
            edit={ UserEdit }
            remove={Delete}
        />
        <Resource
            name="permissions"
            show={ PermissionShow }
            edit={ PermissionEdit }
            create={ PermissionCreate }
            list={ PermissionList }
            remove={Delete}
        />
        <Resource
            name="userdomainroles"
            show={ UserDomainRoleShow }
            create={ UserDomainRoleCreate }
            list={ UserDomainRoleList }
            remove={Delete}
        />
        <Resource
            name="usersiteroles"
            show={ UserSiteRoleShow }
            create={ UserSiteRoleCreate }
            list={ UserSiteRoleList }
            remove={Delete}
        />
    </Admin>
)

export default App;