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
    NumberField,
    NumberInput,
    TextField,
    TextInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateUserSiteRole = values => {
    const errors = {};
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    return errors;
}

export const UserSiteRoleList = props => (
    <List {...props} title="UserSiteRole List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <NumberField source="site_id" />
            <DateField source="created_at" />
            <TextField source="user_id" />
        </Datagrid>
    </List>
)

export const UserSiteRoleShow = props => (
    <Show {...props} title="UserSiteRole Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <NumberField source="site_id" />
            <DateField source="created_at" />
            <TextField source="user_id" />
        </SimpleShowLayout>
    </Show>
)

export const UserSiteRoleCreate = props => (
    <Create {...props} title="Create UserSiteRole">
        <SimpleForm validate={validationCreateUserSiteRole}>
            <NumberInput source="role_id" />
            <NumberInput source="site_id" />
            <TextInput source="user_id" />
        </SimpleForm>
    </Create>
)

