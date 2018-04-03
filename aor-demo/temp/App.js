/**
 * Generated App.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import { cyan500, cyan300 } from 'material-ui/styles/colors';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import { Admin, Delete, Resource } from 'admin-on-rest';
import swaggerRestServer from './swaggerRestServer';
import authClient from './authClient';

import {
    DomainList,
    DomainCreate,
    DomainShow,
    DomainEdit,
} from './Domain';

import {
    DomainRoleList,
    DomainRoleCreate,
    DomainRoleShow,
    DomainRoleEdit,
} from './DomainRole';

import {
    InvitationList,
    InvitationCreate,
    InvitationShow,
    InvitationEdit,
} from './Invitation';

import {
    InvitationDomainRoleList,
    InvitationDomainRoleCreate,
    InvitationDomainRoleShow,
} from './InvitationDomainRole';

import {
    InvitationSiteRoleList,
    InvitationSiteRoleCreate,
    InvitationSiteRoleShow,
} from './InvitationSiteRole';

import {
    PermissionList,
    PermissionCreate,
    PermissionShow,
    PermissionEdit,
} from './Permission';

import {
    ResourceList,
    ResourceCreate,
    ResourceShow,
    ResourceEdit,
} from './Resource';

import {
    RoleList,
    RoleCreate,
    RoleShow,
    RoleEdit,
} from './Role';

import {
    RoleResourcePermissionList,
    RoleResourcePermissionCreate,
    RoleResourcePermissionShow,
} from './RoleResourcePermission';

import {
    SiteList,
    SiteCreate,
    SiteShow,
    SiteEdit,
} from './Site';

import {
    SiteRoleList,
    SiteRoleCreate,
    SiteRoleShow,
    SiteRoleEdit,
} from './SiteRole';

import {
    UserDomainRoleList,
    UserDomainRoleCreate,
    UserDomainRoleShow,
} from './UserDomainRole';

import {
    UserSiteRoleList,
    UserSiteRoleCreate,
    UserSiteRoleShow,
} from './UserSiteRole';

import {
    UserSiteDataList,
    UserSiteDataCreate,
    UserSiteDataShow,
    UserSiteDataEdit,
} from './UserSiteData';

import {
    AdminNoteList,
    AdminNoteCreate,
    AdminNoteShow,
    AdminNoteEdit,
} from './AdminNote';

import {
    SiteDataSchemaList,
    SiteDataSchemaCreate,
    SiteDataSchemaShow,
    SiteDataSchemaEdit,
} from './SiteDataSchema';

import {
    ClientList,
    ClientShow,
} from './Client';

import {
    UserList,
    UserShow,
    UserEdit,
} from './User';



const App = () => (
    <Admin title="Girl Effect Management Portal" theme={getMuiTheme(muiTheme)} restClient={swaggerRestServer('//core-management-layer:8000')} authClient={authClient}>
        <Resource
            name="domains"
            list={ DomainList }
            create={ DomainCreate }
            show={ DomainShow }
            edit={ DomainEdit }
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
            name="invitations"
            list={ InvitationList }
            create={ InvitationCreate }
            show={ InvitationShow }
            edit={ InvitationEdit }
            remove={Delete}
        />
        <Resource
            name="invitationdomainroles"
            list={ InvitationDomainRoleList }
            create={ InvitationDomainRoleCreate }
            show={ InvitationDomainRoleShow }
            remove={Delete}
        />
        <Resource
            name="invitationsiteroles"
            list={ InvitationSiteRoleList }
            create={ InvitationSiteRoleCreate }
            show={ InvitationSiteRoleShow }
            remove={Delete}
        />
        <Resource
            name="permissions"
            list={ PermissionList }
            create={ PermissionCreate }
            show={ PermissionShow }
            edit={ PermissionEdit }
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
            name="roles"
            list={ RoleList }
            create={ RoleCreate }
            show={ RoleShow }
            edit={ RoleEdit }
            remove={Delete}
        />
        <Resource
            name="roleresourcepermissions"
            list={ RoleResourcePermissionList }
            create={ RoleResourcePermissionCreate }
            show={ RoleResourcePermissionShow }
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
            name="siteroles"
            list={ SiteRoleList }
            create={ SiteRoleCreate }
            show={ SiteRoleShow }
            edit={ SiteRoleEdit }
            remove={Delete}
        />
        <Resource
            name="userdomainroles"
            list={ UserDomainRoleList }
            create={ UserDomainRoleCreate }
            show={ UserDomainRoleShow }
            remove={Delete}
        />
        <Resource
            name="usersiteroles"
            list={ UserSiteRoleList }
            create={ UserSiteRoleCreate }
            show={ UserSiteRoleShow }
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
            name="adminnotes"
            list={ AdminNoteList }
            create={ AdminNoteCreate }
            show={ AdminNoteShow }
            edit={ AdminNoteEdit }
            remove={Delete}
        />
        <Resource
            name="sitedataschemas"
            list={ SiteDataSchemaList }
            create={ SiteDataSchemaCreate }
            show={ SiteDataSchemaShow }
            edit={ SiteDataSchemaEdit }
            remove={Delete}
        />
        <Resource
            name="clients"
            list={ ClientList }
            show={ ClientShow }
            remove={Delete}
        />
        <Resource
            name="users"
            list={ UserList }
            show={ UserShow }
            edit={ UserEdit }
            remove={Delete}
        />
    </Admin>
)

const muiTheme = getMuiTheme({
    palette: {
        primary1Color: cyan500,
        accent1Color: cyan300
    }
});

export default App;
/** End of Generated Code **/