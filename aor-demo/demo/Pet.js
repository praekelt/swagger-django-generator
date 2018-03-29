/**
 * Generated Pet.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    TextField,
    SelectField,
    TextInput,
    SelectInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    PetFilter
} from './Filters';

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

export const PetList = props => (
    <List {...props} title="Pet List" filters={<PetFilter />}>
        <Datagrid>
            <NumberField source="id" />
            <TextField source="name" />
            <SelectField source="status" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const PetCreate = props => (
    <Create {...props} title="Pet Create">
        <SimpleForm validate={validationCreatePet}>
            <TextInput source="name" />
            <SelectInput source="status" />
        </SimpleForm>
    </Create>
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

export const PetEdit = props => (
    <Edit {...props} title="Pet Edit">
        <SimpleForm validate={validationEditPet}>
            <TextInput source="name" />
            <SelectInput source="status" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/