/** 
 * Generated Filters.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    Filter,
    TextInput,
    NumberInput,
    BooleanInput
} from 'admin-on-rest';

export const DomainFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
    </Filter>
);

export const DomainRoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <NumberInput label="Domain Id" source="domain_id" />
        <NumberInput label="Role Id" source="role_id" />
    </Filter>
);

export const InvitationFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="Invitor Id" source="invitor_id" />
    </Filter>
);

export const InvitationDomainRoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="Invitation Id" source="invitation_id" />
        <NumberInput label="Domain Id" source="domain_id" />
        <NumberInput label="Role Id" source="role_id" />
    </Filter>
);

export const InvitationSiteRoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="Invitation Id" source="invitation_id" />
        <NumberInput label="Site Id" source="site_id" />
        <NumberInput label="Role Id" source="role_id" />
    </Filter>
);

export const PermissionFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
    </Filter>
);

export const ResourceFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="Prefix" source="prefix" />
    </Filter>
);

export const RoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
    </Filter>
);

export const RoleResourcePermissionFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <NumberInput label="Role Id" source="role_id" />
        <NumberInput label="Resource Id" source="resource_id" />
        <NumberInput label="Permission Id" source="permission_id" />
    </Filter>
);

export const SiteFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
    </Filter>
);

export const SiteRoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <NumberInput label="Site Id" source="site_id" />
        <NumberInput label="Role Id" source="role_id" />
    </Filter>
);

export const UserDomainRoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="User Id" source="user_id" />
        <NumberInput label="Domain Id" source="domain_id" />
        <NumberInput label="Role Id" source="role_id" />
    </Filter>
);

export const UserSiteRoleFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="User Id" source="user_id" />
        <NumberInput label="Site Id" source="site_id" />
        <NumberInput label="Role Id" source="role_id" />
    </Filter>
);

export const UserSiteDataFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="User Id" source="user_id" />
        <NumberInput label="Site Id" source="site_id" />
    </Filter>
);

export const AdminNoteFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="User Id" source="user_id" />
        <TextInput label="Creator Id" source="creator_id" />
    </Filter>
);

export const SiteDataSchemaFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
    </Filter>
);

export const ClientFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="Client Token Id" source="client_token_id" />
    </Filter>
);

export const UserFilter = props => (
    <Filter {...props}>
        <NumberInput label="Offset" source="offset" />
        <NumberInput label="Limit" source="limit" />
        <TextInput label="Email" source="email" />
        <TextInput label="Username Prefix" source="username_prefix" />
    </Filter>
);

/** End of Generated Code **/