import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    TextField,
    TextInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateUser = values => {
    const errors = {};
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.password) {
        errors.password = ["password is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    return errors;
}

const validationEditUser = values => {
    const errors = {};
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    return errors;
}

export const UserList = props => (
    <List {...props} title={"User List"}>
        <DataGrid>
            <TextField source="password" />
            <TextField source="firstName" />
            <TextField source="lastName" />
            <TextField source="phone" />
            <TextField source="email" />
            <TextField source="username" />
            <NumberField source="userStatus" />
            <NumberField source="id" />
            <EditButton />
        </DataGrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title={"User Show"}>
        <SimpleShowLayout>
            <TextField source="password" />
            <TextField source="firstName" />
            <TextField source="lastName" />
            <TextField source="phone" />
            <TextField source="email" />
            <TextField source="username" />
            <NumberField source="userStatus" />
            <NumberField source="id" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const UserCreate = props => (
    <Create {...props} title={"Create User"}>
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="email" />
            <TextInput source="username" />
            <TextInput source="password" />
            <TextInput source="firstName" />
            <TextInput source="lastName" />
            <TextInput source="phone" />
        </SimpleForm>
    </Create>
)

export const UserEdit = props => (
    <Edit {...props} title={"Edit User"}>
        <SimpleForm validate={validationEditUser}>
            <TextInput source="username" />
            <TextInput source="lastName" />
            <TextInput source="phone" />
            <TextInput source="firstName" />
            <TextInput source="email" />
        </SimpleForm>
    </Edit>
)

