/**
 * Generated AdminNote.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    NumberField,
    ReferenceField,
    TextField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    TextInput,
    Show,
    SimpleShowLayout,
    Edit,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    AdminNoteFilter
} from './Filters';

const validationCreateAdminNote = values => {
    const errors = {};
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    if (!values.creator_id) {
        errors.creator_id = ["creator_id is required"];
    }
    if (!values.note) {
        errors.note = ["note is required"];
    }
    return errors;
}

const validationEditAdminNote = values => {
    const errors = {};
    return errors;
}

export const AdminNoteList = props => (
    <List {...props} title="AdminNote List" filters={<AdminNoteFilter />}>
        <Datagrid>
            <NumberField source="id" />
            <ReferenceField label="User" source="user_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <ReferenceField label="User" source="creator_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <TextField source="note" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const AdminNoteCreate = props => (
    <Create {...props} title="AdminNote Create">
        <SimpleForm validate={validationCreateAdminNote}>
            <ReferenceInput label="User" source="user_id" reference="users" allowEmpty>
                <SelectInput source="id" optionText="username" />
            </ReferenceInput>
            <ReferenceInput label="User" source="creator_id" reference="users" allowEmpty>
                <DisabledInput source="id" optionText="username" />
            </ReferenceInput>
            <TextInput source="note" />
        </SimpleForm>
    </Create>
)

export const AdminNoteShow = props => (
    <Show {...props} title="AdminNote Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField label="User" source="user_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <ReferenceField label="User" source="creator_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <TextField source="note" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const AdminNoteEdit = props => (
    <Edit {...props} title="AdminNote Edit">
        <SimpleForm validate={validationEditAdminNote}>
            <TextInput source="note" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/