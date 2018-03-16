import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    SelectField,
    SelectInput,
    TextField,
    TextInput,
    ReferenceField,
    ReferenceInput,
    ReferenceArrayField,
    ReferenceArrayInput,
    SingleFieldList,
    ChipField,
    SelectArrayInput,
    NumberField,
    NumberInput,
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
            <ReferenceField source="category" reference="Category">
                <TextField source="id" />
            </ReferenceField>
            <TextField source="name" />
            <ReferenceArrayField source="tags" reference="Tag">
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
            </ReferenceArrayField>
            <NumberField source="id" />
            <SelectField source="status" />
            <EditButton />
        </DataGrid>
    </List>
)

export const PetShow = props => (
    <Show {...props} title={"Pet Show"}>
        <SimpleShowLayout>
            <ReferenceField source="category" reference="Category">
                <TextField source="id" />
            </ReferenceField>
            <TextField source="name" />
            <ReferenceArrayField source="tags" reference="Tag">
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
            </ReferenceArrayField>
            <NumberField source="id" />
            <SelectField source="status" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const PetCreate = props => (
    <Create {...props} title={"Create Pet"}>
        <SimpleForm validate={validationCreatePet}>
            <TextInput source="name" />
            <ReferenceInput source="category" reference="Category">
                <SelectInput source="id" />
            </ReferenceInput>
            <SelectInput source="status" choices={createchoicestatus} />
            <ReferenceArrayInput source="tags" reference="Tag">
                <SelectArrayInput optionText="id" />
            </ReferenceArrayInput>
        </SimpleForm>
    </Create>
)

export const PetEdit = props => (
    <Edit {...props} title={"Edit Pet"}>
        <SimpleForm validate={validationEditPet}>
            <TextInput source="name" />
            <ReferenceInput source="category" reference="Category">
                <SelectInput source="id" />
            </ReferenceInput>
            <SelectInput source="status" choices={editchoicestatus} />
            <ReferenceArrayInput source="tags" reference="Tag">
                <SelectArrayInput optionText="id" />
            </ReferenceArrayInput>
        </SimpleForm>
    </Edit>
)

