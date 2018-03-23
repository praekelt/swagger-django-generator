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
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
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
    return errors;
}

const validationEditUser = values => {
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
    <List {...props} title="User List">
        <Datagrid>
            <TextField source="phone" />
            <TextField source="firstName" />
            <NumberField source="userStatus" />
            <TextField source="email" />
            <TextField source="username" />
            <TextField source="password" />
            <NumberField source="id" />
            <TextField source="lastName" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserEdit = props => (
    <Edit {...props} title="User Edit">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="username" />
            <TextInput source="phone" />
            <TextInput source="email" />
            <TextInput source="lastName" />
            <TextInput source="firstName" />
        </SimpleForm>
    </Edit>
)

export const UserShow = props => (
    <Show {...props} title="User Show">
        <SimpleShowLayout>
            <TextField source="phone" />
            <TextField source="firstName" />
            <NumberField source="userStatus" />
            <TextField source="email" />
            <TextField source="username" />
            <TextField source="password" />
            <NumberField source="id" />
            <TextField source="lastName" />
        </SimpleShowLayout>
    </Show>
)

export const UserCreate = props => (
    <Create {...props} title="User Create">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="username" />
            <TextInput source="email" />
            <TextInput source="lastName" />
            <TextInput source="phone" />
            <TextInput source="password" />
            <TextInput source="firstName" />
        </SimpleForm>
    </Create>
)

