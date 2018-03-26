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
    TextField,
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateUser = values => {
    const errors = {};
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.password) {
        errors.password = ["password is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    return errors;
}

const validationEditUser = values => {
    const errors = {};
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.username) {
        errors.username = ["username is required"];
    }
    return errors;
}

export const UserList = props => (
    <List {...props} title="User List">
        <Datagrid>
            <NumberField source="userStatus" />
            <TextField source="username" />
            <TextField source="email" />
            <NumberField source="id" />
            <TextField source="lastName" />
            <TextField source="phone" />
            <TextField source="password" />
            <TextField source="firstName" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title="User Show">
        <SimpleShowLayout>
            <NumberField source="userStatus" />
            <TextField source="username" />
            <TextField source="email" />
            <NumberField source="id" />
            <TextField source="lastName" />
            <TextField source="phone" />
            <TextField source="password" />
            <TextField source="firstName" />
        </SimpleShowLayout>
    </Show>
)

export const UserEdit = props => (
    <Edit {...props} title="User Edit">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="lastName" />
            <TextInput source="phone" />
            <TextInput source="email" />
            <TextInput source="firstName" />
            <TextInput source="username" />
        </SimpleForm>
    </Edit>
)

export const UserCreate = props => (
    <Create {...props} title="User Create">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="username" />
            <TextInput source="lastName" />
            <TextInput source="phone" />
            <TextInput source="password" />
            <TextInput source="firstName" />
            <TextInput source="email" />
        </SimpleForm>
    </Create>
)

