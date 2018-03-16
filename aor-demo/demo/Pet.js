import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    NumberInput,
    SelectField,
    SelectInput,
    TextField,
    TextInput,
    DisabledInput,
    EditButton

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

export const PetList = props => (
    <List {...props} title={"Pet List"}>
        <DataGrid>
            <NumberField source="id" />
            <SelectField source="status" />
            <TextField source="photoUrls" />
            <TextField source="name" />
            <EditButton />
        </DataGrid>
    </List>
)

export const PetShow = props => (
    <Show {...props} title={"Pet Show"}>
        <SimpleShowLayout>
            <NumberField source="id" />
            <SelectField source="status" />
            <TextField source="photoUrls" />
            <TextField source="name" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const PetCreate = props => (
    <Create {...props} title={"Create Pet"}>
        <SimpleForm validate={validationCreatePet}>
            <TextInput source="name" />
            <SelectInput source="status" choices={createchoicestatus} />
            <TextInput source="photoUrls" />
        </SimpleForm>
    </Create>
)

export const PetEdit = props => (
    <Edit {...props} title={"Edit Pet"}>
        <SimpleForm validate={validationEditPet}>
            <TextInput source="name" />
            <SelectInput source="status" choices={editchoicestatus} />
            <TextInput source="photoUrls" />
        </SimpleForm>
    </Edit>
)

