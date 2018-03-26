import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    TextInput,
    SelectInput,
    NumberField,
    TextField,
    SelectField,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreatePet = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditPet = values => {
    const errors = {};
    return errors;
}

const createchoicestatus = [
    { id: 'available', name: 'available' },
    { id: 'pending', name: 'pending' },
    { id: 'sold', name: 'sold' },
];

const editchoicestatus = [
    { id: 'available', name: 'available' },
    { id: 'pending', name: 'pending' },
    { id: 'sold', name: 'sold' },
];

export const PetEdit = props => (
    <Edit {...props} title="Pet Edit">
        <SimpleForm validate={validationCreatePet}>
            <TextInput source="name" />
            <SelectInput source="status" />
        </SimpleForm>
    </Edit>
)

export const PetShow = props => (
    <Show {...props} title="Pet Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="name" />
            <SelectField source="status" />
        </SimpleShowLayout>
    </Show>
)

export const PetCreate = props => (
    <Create {...props} title="Pet Create">
        <SimpleForm validate={validationCreatePet}>
            <TextInput source="name" />
            <SelectInput source="status" />
        </SimpleForm>
    </Create>
)

