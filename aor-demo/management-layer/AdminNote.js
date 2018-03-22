import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    DateField,
    DateInput,
    TextField,
    TextInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateAdminNote = values => {
    const errors = {};
    if (!values.note) {
        errors.note = ["note is required"];
    }
    if (!values.creator_id) {
        errors.creator_id = ["creator_id is required"];
    }
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    return errors;
}

const validationEditAdminNote = values => {
    const errors = {};
    return errors;
}

export const AdminNoteList = props => (
    <List {...props} title="AdminNote List">
        <Datagrid>
            <DateField source="updated_at" />
            <TextField source="creator_id" />
            <TextField source="user_id" />
            <TextField source="note" />
            <NumberField source="id" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const AdminNoteShow = props => (
    <Show {...props} title="AdminNote Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <TextField source="creator_id" />
            <TextField source="user_id" />
            <TextField source="note" />
            <NumberField source="id" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const AdminNoteCreate = props => (
    <Create {...props} title="Create AdminNote">
        <SimpleForm validate={validationCreateAdminNote}>
            <TextInput source="note" />
            <TextInput source="creator_id" />
            <TextInput source="user_id" />
        </SimpleForm>
    </Create>
)

export const AdminNoteEdit = props => (
    <Edit {...props} title="Edit AdminNote">
        <SimpleForm validate={validationEditAdminNote}>
            <TextInput source="note" />
        </SimpleForm>
    </Edit>
)

