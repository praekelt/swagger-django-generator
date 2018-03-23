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
    NumberField,
    TextField,
    TextInput,
    NumberInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateDomain = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditDomain = values => {
    const errors = {};
    return errors;
}

export const DomainShow = props => (
    <Show {...props} title="Domain Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="id" />
            <NumberField source="parent_id" />
            <DateField source="created_at" />
            <TextField source="description" />
            <TextField source="name" />
        </SimpleShowLayout>
    </Show>
)

export const DomainEdit = props => (
    <Edit {...props} title="Domain Edit">
        <SimpleForm validate={validationCreateDomain}>
            <TextInput source="description" />
            <NumberInput source="parent_id" />
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
)

export const DomainCreate = props => (
    <Create {...props} title="Domain Create">
        <SimpleForm validate={validationCreateDomain}>
            <TextInput source="description" />
            <NumberInput source="parent_id" />
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

export const DomainList = props => (
    <List {...props} title="Domain List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="id" />
            <NumberField source="parent_id" />
            <DateField source="created_at" />
            <TextField source="description" />
            <TextField source="name" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

