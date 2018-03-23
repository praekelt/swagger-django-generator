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
    TextField,
    NumberField,
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreatePermission = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditPermission = values => {
    const errors = {};
    return errors;
}

export const PermissionShow = props => (
    <Show {...props} title="Permission Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <TextField source="description" />
            <DateField source="created_at" />
            <NumberField source="id" />
            <TextField source="name" />
        </SimpleShowLayout>
    </Show>
)

export const PermissionEdit = props => (
    <Edit {...props} title="Permission Edit">
        <SimpleForm validate={validationCreatePermission}>
            <TextInput source="description" />
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
)

export const PermissionCreate = props => (
    <Create {...props} title="Permission Create">
        <SimpleForm validate={validationCreatePermission}>
            <TextInput source="description" />
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

export const PermissionList = props => (
    <List {...props} title="Permission List">
        <Datagrid>
            <DateField source="updated_at" />
            <TextField source="description" />
            <DateField source="created_at" />
            <NumberField source="id" />
            <TextField source="name" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

