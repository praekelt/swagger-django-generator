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
    BooleanField,
    DateField,
    TextInput,
    BooleanInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationEditUser = values => {
    const errors = {};
    return errors;
}

export const UserList = props => (
    <List {...props} title="User List">
        <Datagrid>
            <TextField source="last_name" />
            <TextField source="username" />
            <TextField source="country_code" />
            <BooleanField source="msisdn_verified" />
            <DateField source="created_at" />
            <BooleanField source="is_active" />
            <DateField source="last_login" />
            <TextField source="email" />
            <BooleanField source="email_verified" />
            <TextField source="birth_date" />
            <DateField source="updated_at" />
            <TextField source="date_joined" />
            <TextField source="first_name" />
            <TextField source="id" />
            <TextField source="msisdn" />
            <TextField source="avatar" />
            <TextField source="gender" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title="User Show">
        <SimpleShowLayout>
            <TextField source="last_name" />
            <TextField source="username" />
            <TextField source="country_code" />
            <BooleanField source="msisdn_verified" />
            <DateField source="created_at" />
            <BooleanField source="is_active" />
            <DateField source="last_login" />
            <TextField source="email" />
            <BooleanField source="email_verified" />
            <TextField source="birth_date" />
            <DateField source="updated_at" />
            <TextField source="date_joined" />
            <TextField source="first_name" />
            <TextField source="id" />
            <TextField source="msisdn" />
            <TextField source="avatar" />
            <TextField source="gender" />
        </SimpleShowLayout>
    </Show>
)

export const UserEdit = props => (
    <Edit {...props} title="User Edit">
        <SimpleForm validate={validationCreateUser}>
            <TextInput source="last_name" />
            <TextInput source="email" />
            <TextInput source="country_code" />
            <BooleanInput source="is_active" />
            <BooleanInput source="email_verified" />
            <BooleanInput source="msisdn_verified" />
            <TextInput source="birth_date" />
            <TextInput source="first_name" />
            <TextInput source="msisdn" />
            <TextInput source="avatar" />
            <TextInput source="gender" />
        </SimpleForm>
    </Edit>
)

