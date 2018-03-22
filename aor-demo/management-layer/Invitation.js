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
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateInvitation = values => {
    const errors = {};
    if (!values.email) {
        errors.email = ["email is required"];
    }
    if (!values.first_name) {
        errors.first_name = ["first_name is required"];
    }
    if (!values.last_name) {
        errors.last_name = ["last_name is required"];
    }
    if (!values.invitor_id) {
        errors.invitor_id = ["invitor_id is required"];
    }
    return errors;
}

const validationEditInvitation = values => {
    const errors = {};
    return errors;
}

export const InvitationList = props => (
    <List {...props} title="Invitation List">
        <Datagrid>
            <TextField source="email" />
            <TextField source="last_name" />
            <TextField source="first_name" />
            <DateField source="expires_at" />
            <DateField source="updated_at" />
            <TextField source="id" />
            <DateField source="created_at" />
            <TextField source="invitor_id" />
            <EditButton />
        </Datagrid>
    </List>
)

export const InvitationShow = props => (
    <Show {...props} title="Invitation Show">
        <SimpleShowLayout>
            <TextField source="email" />
            <TextField source="last_name" />
            <TextField source="first_name" />
            <DateField source="expires_at" />
            <DateField source="updated_at" />
            <TextField source="id" />
            <DateField source="created_at" />
            <TextField source="invitor_id" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const InvitationCreate = props => (
    <Create {...props} title="Create Invitation">
        <SimpleForm validate={validationCreateInvitation}>
            <TextInput source="email" />
            <TextInput source="first_name" />
            <TextInput source="last_name" />
            <DateInput source="expires_at" />
            <TextInput source="invitor_id" />
        </SimpleForm>
    </Create>
)

export const InvitationEdit = props => (
    <Edit {...props} title="Edit Invitation">
        <SimpleForm validate={validationEditInvitation}>
            <TextInput source="email" />
            <TextInput source="first_name" />
            <TextInput source="last_name" />
            <DateInput source="expires_at" />
        </SimpleForm>
    </Edit>
)

