import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    TextField,
    TextInput,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

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

export const PermissionList = props => (
    <List {...props} title="Permission List">
        <Datagrid>
            <TextField source="name" />
            <DateField source="updated_at" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const PermissionShow = props => (
    <Show {...props} title="Permission Show">
        <SimpleShowLayout>
            <TextField source="name" />
            <DateField source="updated_at" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const PermissionCreate = props => (
    <Create {...props} title="Create Permission">
        <SimpleForm validate={validationCreatePermission}>
            <TextInput source="name" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const PermissionEdit = props => (
    <Edit {...props} title="Edit Permission">
        <SimpleForm validate={validationEditPermission}>
            <TextInput source="name" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

