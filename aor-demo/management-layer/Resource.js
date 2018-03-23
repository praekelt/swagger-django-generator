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
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateResource = values => {
    const errors = {};
    if (!values.urn) {
        errors.urn = ["urn is required"];
    }
    return errors;
}

const validationEditResource = values => {
    const errors = {};
    return errors;
}

export const ResourceList = props => (
    <List {...props} title="Resource List">
        <Datagrid>
            <TextField source="urn" />
            <NumberField source="id" />
            <DateField source="created_at" />
            <TextField source="description" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const ResourceCreate = props => (
    <Create {...props} title="Resource Create">
        <SimpleForm validate={validationCreateResource}>
            <TextInput source="urn" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const ResourceShow = props => (
    <Show {...props} title="Resource Show">
        <SimpleShowLayout>
            <TextField source="urn" />
            <NumberField source="id" />
            <DateField source="created_at" />
            <TextField source="description" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const ResourceEdit = props => (
    <Edit {...props} title="Resource Edit">
        <SimpleForm validate={validationCreateResource}>
            <TextInput source="urn" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

