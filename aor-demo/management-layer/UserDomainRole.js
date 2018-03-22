import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    NumberInput,
    DateField,
    DateInput,
    TextField,
    TextInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateUserDomainRole = values => {
    const errors = {};
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    return errors;
}

export const UserDomainRoleList = props => (
    <List {...props} title="UserDomainRole List">
        <Datagrid>
            <NumberField source="domain_id" />
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <DateField source="created_at" />
            <TextField source="user_id" />
        </Datagrid>
    </List>
)

export const UserDomainRoleShow = props => (
    <Show {...props} title="UserDomainRole Show">
        <SimpleShowLayout>
            <NumberField source="domain_id" />
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <DateField source="created_at" />
            <TextField source="user_id" />
        </SimpleShowLayout>
    </Show>
)

export const UserDomainRoleCreate = props => (
    <Create {...props} title="Create UserDomainRole">
        <SimpleForm validate={validationCreateUserDomainRole}>
            <NumberInput source="domain_id" />
            <NumberInput source="role_id" />
            <TextInput source="user_id" />
        </SimpleForm>
    </Create>
)

