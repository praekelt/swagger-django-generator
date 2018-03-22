import React from 'react';
import { simpleRestClient, Admin, Resource } from 'admin-on-rest';
import { Delete } from 'admin-on-rest/lib/mui';

import { 
    SiteList,
    SiteShow,
    SiteCreate,
    SiteEdit
} from './site';
import { 
    AdminNoteList,
    AdminNoteShow,
    AdminNoteCreate,
    AdminNoteEdit
} from './admin-note';
import { 
    InvitationDomainRoleList,
    InvitationDomainRoleShow,
    InvitationDomainRoleCreate
} from './invitation-domain-role';
import { 
    InvitationSiteRoleList,
    InvitationSiteRoleShow,
    InvitationSiteRoleCreate
} from './invitation-site-role';
import { 
    SiteAndDomainRolesList,
    SiteAndDomainRolesShow
} from './site-and-domain-roles';
import { 
    ClientList,
    ClientShow
} from './client';
import { 
    UserList,
    UserShow,
    UserEdit
} from './user';
import { 
    DomainList,
    DomainShow,
    DomainCreate,
    DomainEdit
} from './domain';
import { 
    PermissionList,
    PermissionShow,
    PermissionCreate,
    PermissionEdit
} from './permission';
import { 
    AllUserRolesList,
    AllUserRolesShow
} from './all-user-roles';
import { 
    RoleResourcePermissionList,
    RoleResourcePermissionShow,
    RoleResourcePermissionCreate
} from './role-resource-permission';
import { 
    UserSiteRoleLabelsAggregatedList,
    UserSiteRoleLabelsAggregatedShow
} from './user-site-role-labels-aggregated';
import { 
    InvitationList,
    InvitationShow,
    InvitationCreate,
    InvitationEdit
} from './invitation';
import { 
    SiteDataSchemaList,
    SiteDataSchemaShow,
    SiteDataSchemaCreate,
    SiteDataSchemaEdit
} from './site-data-schema';
import { 
    SiteRoleList,
    SiteRoleShow,
    SiteRoleCreate,
    SiteRoleEdit
} from './site-role';
import { 
    ResourceList,
    ResourceShow,
    ResourceCreate,
    ResourceEdit
} from './resource';
import { 
    DomainRoleList,
    DomainRoleShow,
    DomainRoleCreate,
    DomainRoleEdit
} from './domain-role';
import { 
    UserSiteRoleList,
    UserSiteRoleShow,
    UserSiteRoleCreate
} from './user-site-role';
import { 
    SiteRoleLabelsAggregatedList,
    SiteRoleLabelsAggregatedShow
} from './site-role-labels-aggregated';
import { 
    RoleList,
    RoleShow,
    RoleCreate,
    RoleEdit
} from './role';
import { 
    UserSiteDataList,
    UserSiteDataShow,
    UserSiteDataCreate,
    UserSiteDataEdit
} from './user-site-data';
import { 
    DomainRolesList,
    DomainRolesShow
} from './domain-roles';
import { 
    UserDomainRoleList,
    UserDomainRoleShow,
    UserDomainRoleCreate
} from './user-domain-role';


const App = () => (
    <Admin title={"ManagementLayer"} restClient={simpleRestClient}>
        <Resource
            name="site"
            list={ SiteList }
            show={ SiteShow }
            create={ SiteCreate }
            edit={ SiteEdit}
            remove={Delete}
        />
        <Resource
            name="admin-note"
            list={ AdminNoteList }
            show={ AdminNoteShow }
            create={ AdminNoteCreate }
            edit={ AdminNoteEdit}
            remove={Delete}
        />
        <Resource
            name="invitation-domain-role"
            list={ InvitationDomainRoleList }
            show={ InvitationDomainRoleShow }
            create={ InvitationDomainRoleCreate }
            remove={Delete}
        />
        <Resource
            name="invitation-site-role"
            list={ InvitationSiteRoleList }
            show={ InvitationSiteRoleShow }
            create={ InvitationSiteRoleCreate }
            remove={Delete}
        />
        <Resource
            name="site-and-domain-roles"
            list={ SiteAndDomainRolesList }
            show={ SiteAndDomainRolesShow }
            remove={Delete}
        />
        <Resource
            name="client"
            list={ ClientList }
            show={ ClientShow }
            remove={Delete}
        />
        <Resource
            name="user"
            list={ UserList }
            show={ UserShow }
            edit={ UserEdit}
            remove={Delete}
        />
        <Resource
            name="domain"
            list={ DomainList }
            show={ DomainShow }
            create={ DomainCreate }
            edit={ DomainEdit}
            remove={Delete}
        />
        <Resource
            name="permission"
            list={ PermissionList }
            show={ PermissionShow }
            create={ PermissionCreate }
            edit={ PermissionEdit}
            remove={Delete}
        />
        <Resource
            name="all-user-roles"
            list={ AllUserRolesList }
            show={ AllUserRolesShow }
            remove={Delete}
        />
        <Resource
            name="role-resource-permission"
            list={ RoleResourcePermissionList }
            show={ RoleResourcePermissionShow }
            create={ RoleResourcePermissionCreate }
            remove={Delete}
        />
        <Resource
            name="user-site-role-labels-aggregated"
            list={ UserSiteRoleLabelsAggregatedList }
            show={ UserSiteRoleLabelsAggregatedShow }
            remove={Delete}
        />
        <Resource
            name="invitation"
            list={ InvitationList }
            show={ InvitationShow }
            create={ InvitationCreate }
            edit={ InvitationEdit}
            remove={Delete}
        />
        <Resource
            name="site-data-schema"
            list={ SiteDataSchemaList }
            show={ SiteDataSchemaShow }
            create={ SiteDataSchemaCreate }
            edit={ SiteDataSchemaEdit}
            remove={Delete}
        />
        <Resource
            name="site-role"
            list={ SiteRoleList }
            show={ SiteRoleShow }
            create={ SiteRoleCreate }
            edit={ SiteRoleEdit}
            remove={Delete}
        />
        <Resource
            name="resource"
            list={ ResourceList }
            show={ ResourceShow }
            create={ ResourceCreate }
            edit={ ResourceEdit}
            remove={Delete}
        />
        <Resource
            name="domain-role"
            list={ DomainRoleList }
            show={ DomainRoleShow }
            create={ DomainRoleCreate }
            edit={ DomainRoleEdit}
            remove={Delete}
        />
        <Resource
            name="user-site-role"
            list={ UserSiteRoleList }
            show={ UserSiteRoleShow }
            create={ UserSiteRoleCreate }
            remove={Delete}
        />
        <Resource
            name="site-role-labels-aggregated"
            list={ SiteRoleLabelsAggregatedList }
            show={ SiteRoleLabelsAggregatedShow }
            remove={Delete}
        />
        <Resource
            name="role"
            list={ RoleList }
            show={ RoleShow }
            create={ RoleCreate }
            edit={ RoleEdit}
            remove={Delete}
        />
        <Resource
            name="user-site-data"
            list={ UserSiteDataList }
            show={ UserSiteDataShow }
            create={ UserSiteDataCreate }
            edit={ UserSiteDataEdit}
            remove={Delete}
        />
        <Resource
            name="domain-roles"
            list={ DomainRolesList }
            show={ DomainRolesShow }
            remove={Delete}
        />
        <Resource
            name="user-domain-role"
            list={ UserDomainRoleList }
            show={ UserDomainRoleShow }
            create={ UserDomainRoleCreate }
            remove={Delete}
        />
    </Admin>
)

export default App;