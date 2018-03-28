/**
 * Generated User.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
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
import {
    UserFilter
} from './Filter';

const validationCreateUser = values => {
    const errors = {};
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.password) {
        errors.password = ["password is required"];
    }
    return errors;
}

const validationEditUser = values => {
    const errors = {};
    if (!values.username) {
        errors.username = ["username is required"];
    }
    if (!values.firstName) {
        errors.firstName = ["firstName is required"];
    }
    if (!values.lastName) {
        errors.lastName = ["lastName is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    return errors;
}

export const UserList = props => (
    <List {...props} title="User List" filters={<UserFilter />}>
        <Datagrid>
            <NumberField source="id" />
            <TextField source="username" />
            <TextField source="firstName" />
            <TextField source="lastName" />
            <TextField source="email" />
            <TextField source="password" />
            <TextField source="phone" />
            <NumberField source="userStatus" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserCreate = props => (
    <Create {...props} title="User Create">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="username" />
            <TextInput source="firstName" />
            <TextInput source="lastName" />
            <TextInput source="email" />
            <TextInput source="password" />
            <TextInput source="phone" />
        </SimpleForm>
    </Create>
)

export const UserShow = props => (
    <Show {...props} title="User Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="username" />
            <TextField source="firstName" />
            <TextField source="lastName" />
            <TextField source="email" />
            <TextField source="password" />
            <TextField source="phone" />
            <NumberField source="userStatus" />
        </SimpleShowLayout>
    </Show>
)

export const UserEdit = props => (
    <Edit {...props} title="User Edit">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="username" />
            <TextInput source="firstName" />
            <TextInput source="lastName" />
            <TextInput source="email" />
            <TextInput source="phone" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/