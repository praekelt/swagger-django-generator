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
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateuser = values => {
    const errors = {};
    if (!values.password) {
        errors.password = ["password is required"];
    }
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    return errors;
}

const validationEdituser = values => {
    const errors = {};
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    return errors;
}

export const UserList = props => (
    <List {...props} title="user List">
        <Datagrid>
            <TextField source="password" />
            <TextField source="username" />
            <TextField source="lastName" />
            <TextField source="firstName" />
            <NumberField source="userStatus" />
            <NumberField source="id" />
            <TextField source="phone" />
            <TextField source="email" />
            <EditButton />
        </Datagrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title="user Show">
        <SimpleShowLayout>
            <TextField source="password" />
            <TextField source="username" />
            <TextField source="lastName" />
            <TextField source="firstName" />
            <NumberField source="userStatus" />
            <NumberField source="id" />
            <TextField source="phone" />
            <TextField source="email" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const UserCreate = props => (
    <Create {...props} title="Create user">
        <SimpleForm validate={validationCreateuser}>
            <TextInput source="password" />
            <TextInput source="username" />
            <TextInput source="lastName" />
            <TextInput source="phone" />
            <TextInput source="email" />
            <TextInput source="firstName" />
        </SimpleForm>
    </Create>
)

export const UserEdit = props => (
    <Edit {...props} title="Edit user">
        <SimpleForm validate={validationEdituser}>
            <TextInput source="username" />
            <TextInput source="phone" />
            <TextInput source="email" />
            <TextInput source="lastName" />
            <TextInput source="firstName" />
        </SimpleForm>
    </Edit>
)

