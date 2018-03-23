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
    NumberField,
    DateField,
    BooleanField,
    TextInput,
    BooleanInput,
    NumberInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateSite = values => {
    const errors = {};
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditSite = values => {
    const errors = {};
    return errors;
}

export const SiteList = props => (
    <List {...props} title="Site List">
        <Datagrid>
            <TextField source="client_id" />
            <NumberField source="id" />
            <NumberField source="domain_id" />
            <TextField source="name" />
            <DateField source="updated_at" />
            <DateField source="created_at" />
            <TextField source="description" />
            <BooleanField source="is_active" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const SiteCreate = props => (
    <Create {...props} title="Site Create">
        <SimpleForm validate={validationCreateSite}>
            <TextInput source="client_id" />
            <TextInput source="description" />
            <BooleanInput source="is_active" />
            <NumberInput source="domain_id" />
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

export const SiteShow = props => (
    <Show {...props} title="Site Show">
        <SimpleShowLayout>
            <TextField source="client_id" />
            <NumberField source="id" />
            <NumberField source="domain_id" />
            <TextField source="name" />
            <DateField source="updated_at" />
            <DateField source="created_at" />
            <TextField source="description" />
            <BooleanField source="is_active" />
        </SimpleShowLayout>
    </Show>
)

export const SiteEdit = props => (
    <Edit {...props} title="Site Edit">
        <SimpleForm validate={validationCreateSite}>
            <TextInput source="client_id" />
            <TextInput source="description" />
            <BooleanInput source="is_active" />
            <NumberInput source="domain_id" />
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
)

