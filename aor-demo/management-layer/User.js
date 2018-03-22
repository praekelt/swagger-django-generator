import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    BooleanField,
    BooleanInput,
    TextField,
    TextInput,
    DateField,
    DateInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationEditUser = values => {
    const errors = {};
    return errors;
}

export const UserList = props => (
    <List {...props} title="User List">
        <Datagrid>
            <BooleanField source="is_active" />
            <TextField source="last_name" />
            <BooleanField source="msisdn_verified" />
            <TextField source="msisdn" />
            <TextField source="avatar" />
            <TextField source="country_code" />
            <TextField source="id" />
            <DateField source="created_at" />
            <TextField source="email" />
            <TextField source="gender" />
            <TextField source="birth_date" />
            <BooleanField source="email_verified" />
            <TextField source="first_name" />
            <DateField source="updated_at" />
            <DateField source="last_login" />
            <TextField source="date_joined" />
            <TextField source="username" />
            <EditButton />
        </Datagrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title="User Show">
        <SimpleShowLayout>
            <BooleanField source="is_active" />
            <TextField source="last_name" />
            <BooleanField source="msisdn_verified" />
            <TextField source="msisdn" />
            <TextField source="avatar" />
            <TextField source="country_code" />
            <TextField source="id" />
            <DateField source="created_at" />
            <TextField source="email" />
            <TextField source="gender" />
            <TextField source="birth_date" />
            <BooleanField source="email_verified" />
            <TextField source="first_name" />
            <DateField source="updated_at" />
            <DateField source="last_login" />
            <TextField source="date_joined" />
            <TextField source="username" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const UserEdit = props => (
    <Edit {...props} title="Edit User">
        <SimpleForm validate={validationEditUser}>
            <TextInput source="email" />
            <BooleanInput source="is_active" />
            <TextInput source="last_name" />
            <BooleanInput source="msisdn_verified" />
            <TextInput source="birth_date" />
            <BooleanInput source="email_verified" />
            <TextInput source="first_name" />
            <TextInput source="msisdn" />
            <TextInput source="avatar" />
            <TextInput source="country_code" />
            <TextInput source="gender" />
        </SimpleForm>
    </Edit>
)

