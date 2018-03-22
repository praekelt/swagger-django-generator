import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    DateField,
    DateInput,
    TextField,
    TextInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateInvitationSiteRole = values => {
    const errors = {};
    if (!values.invitation_id) {
        errors.invitation_id = ["invitation_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    return errors;
}

export const InvitationSiteRoleList = props => (
    <List {...props} title="InvitationSiteRole List">
        <Datagrid>
            <DateField source="updated_at" />
            <TextField source="invitation_id" />
            <NumberField source="role_id" />
            <NumberField source="site_id" />
            <DateField source="created_at" />
        </Datagrid>
    </List>
)

export const InvitationSiteRoleShow = props => (
    <Show {...props} title="InvitationSiteRole Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <TextField source="invitation_id" />
            <NumberField source="role_id" />
            <NumberField source="site_id" />
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
)

export const InvitationSiteRoleCreate = props => (
    <Create {...props} title="Create InvitationSiteRole">
        <SimpleForm validate={validationCreateInvitationSiteRole}>
            <TextInput source="invitation_id" />
            <NumberInput source="role_id" />
            <NumberInput source="site_id" />
        </SimpleForm>
    </Create>
)

