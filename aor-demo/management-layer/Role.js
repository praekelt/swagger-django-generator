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
    BooleanField,
    BooleanInput,
    NumberField,
    NumberInput,
    TextField,
    TextInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateRole = values => {
    const errors = {};
    if (!values.requires_2fa) {
        errors.requires_2fa = ["requires_2fa is required"];
    }
    return errors;
}

const validationEditRole = values => {
    const errors = {};
    return errors;
}

export const RoleList = props => (
    <List {...props} title="Role List">
        <Datagrid>
            <DateField source="updated_at" />
            <BooleanField source="requires_2fa" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const RoleShow = props => (
    <Show {...props} title="Role Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <BooleanField source="requires_2fa" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const RoleCreate = props => (
    <Create {...props} title="Create Role">
        <SimpleForm validate={validationCreateRole}>
            <BooleanInput source="requires_2fa" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const RoleEdit = props => (
    <Edit {...props} title="Edit Role">
        <SimpleForm validate={validationEditRole}>
            <BooleanInput source="requires_2fa" />
            <TextInput source="label" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

