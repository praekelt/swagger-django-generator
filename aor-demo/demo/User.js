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
    NumberField,
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateUser = values => {
    const errors = {};
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.password) {
        errors.password = ["password is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
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
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    return errors;
}

export const UserList = props => (
    <List {...props} title="User List">
        <Datagrid>
            <TextField source="lastName" />
            <NumberField source="id" />
            <NumberField source="userStatus" />
            <TextField source="password" />
            <TextField source="phone" />
            <TextField source="email" />
            <TextField source="username" />
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
            <TextField source="lastName" />
            <NumberField source="id" />
            <NumberField source="userStatus" />
            <TextField source="password" />
            <TextField source="phone" />
            <TextField source="email" />
            <TextField source="username" />
            <TextField source="firstName" />
        </SimpleShowLayout>
    </Show>
)

export const UserCreate = props => (
    <Create {...props} title="User Create">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="lastName" />
            <TextInput source="password" />
            <TextInput source="phone" />
            <TextInput source="email" />
            <TextInput source="username" />
            <TextInput source="firstName" />
        </SimpleForm>
    </Create>
)

export const UserEdit = props => (
    <Edit {...props} title="User Edit">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="lastName" />
            <TextInput source="email" />
            <TextInput source="phone" />
            <TextInput source="username" />
            <TextInput source="firstName" />
        </SimpleForm>
    </Edit>
)

