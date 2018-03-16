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
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.password) {
        errors.password = ["password is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    return errors;
}

const validationEditUser = values => {
    const errors = {};
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.username) {
        errors.username = ["username is required"];
    }
    return errors;
}

export const UserList = props => (
    <List {...props} title={"User List"}>
        <DataGrid>
            <TextField source="firstName" />
            <TextField source="password" />
            <NumberField source="id" />
            <TextField source="lastName" />
            <TextField source="phone" />
            <TextField source="username" />
            <TextField source="email" />
            <NumberField source="userStatus" />
            <EditButton />
        </DataGrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title={"User Show"}>
        <SimpleShowLayout>
            <TextField source="firstName" />
            <TextField source="password" />
            <NumberField source="id" />
            <TextField source="lastName" />
            <TextField source="phone" />
            <TextField source="username" />
            <TextField source="email" />
            <NumberField source="userStatus" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const UserCreate = props => (
    <Create {...props} title={"Create User"}>
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="phone" />
            <TextInput source="firstName" />
            <TextInput source="username" />
            <TextInput source="password" />
            <TextInput source="email" />
            <TextInput source="lastName" />
        </SimpleForm>
    </Create>
)

export const UserEdit = props => (
    <Edit {...props} title={"Edit User"}>
        <SimpleForm validate={validationEditUser}>
            <TextInput source="email" />
            <TextInput source="phone" />
            <TextInput source="firstName" />
            <TextInput source="lastName" />
            <TextInput source="username" />
        </SimpleForm>
    </Edit>
)

