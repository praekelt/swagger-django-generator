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
    NumberField,
    TextField,
    BooleanField,
    TextInput,
    BooleanInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
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
            <NumberField source="id" />
            <DateField source="created_at" />
            <TextField source="description" />
            <BooleanField source="requires_2fa" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const RoleCreate = props => (
    <Create {...props} title="Role Create">
        <SimpleForm validate={validationCreateRole}>
            <TextInput source="description" />
            <BooleanInput source="requires_2fa" />
        </SimpleForm>
    </Create>
)

export const RoleShow = props => (
    <Show {...props} title="Role Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="id" />
            <DateField source="created_at" />
            <TextField source="description" />
            <BooleanField source="requires_2fa" />
        </SimpleShowLayout>
    </Show>
)

export const RoleEdit = props => (
    <Edit {...props} title="Role Edit">
        <SimpleForm validate={validationCreateRole}>
            <TextInput source="description" />
            <TextInput source="label" />
            <BooleanInput source="requires_2fa" />
        </SimpleForm>
    </Edit>
)

