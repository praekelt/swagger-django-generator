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
    DateField,
    DateInput,
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateInvitation = values => {
    const errors = {};
    if (!values.last_name) {
        errors.last_name = ["last_name is required"];
    }
    if (!values.invitor_id) {
        errors.invitor_id = ["invitor_id is required"];
    }
    if (!values.first_name) {
        errors.first_name = ["first_name is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
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
            <TextField source="id" />
            <TextField source="email" />
            <DateField source="expires_at" />
            <TextField source="invitor_id" />
            <TextField source="last_name" />
            <DateField source="updated_at" />
            <TextField source="first_name" />
            <DateField source="created_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const InvitationCreate = props => (
    <Create {...props} title="Invitation Create">
        <SimpleForm validate={validationCreateInvitation}>
            <DateInput source="expires_at" />
            <TextInput source="last_name" />
            <TextInput source="invitor_id" />
            <TextInput source="first_name" />
            <TextInput source="email" />
        </SimpleForm>
    </Create>
)

export const InvitationShow = props => (
    <Show {...props} title="Invitation Show">
        <SimpleShowLayout>
            <TextField source="id" />
            <TextField source="email" />
            <DateField source="expires_at" />
            <TextField source="invitor_id" />
            <TextField source="last_name" />
            <DateField source="updated_at" />
            <TextField source="first_name" />
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
)

export const InvitationEdit = props => (
    <Edit {...props} title="Invitation Edit">
        <SimpleForm validate={validationCreateInvitation}>
            <DateInput source="expires_at" />
            <TextInput source="last_name" />
            <TextInput source="first_name" />
            <TextInput source="email" />
        </SimpleForm>
    </Edit>
)

