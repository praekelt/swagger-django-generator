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
    TextInput,
    SelectField,
    SelectInput,
    NumberField,
    NumberInput,
    ReferenceField,
    ReferenceInput,
    ReferenceArrayField,
    ReferenceArrayInput,
    SingleFieldList,
    ChipField,
    SelectArrayInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreatepet = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditpet = values => {
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
    <List {...props} title="pet List">
        <Datagrid>
            <TextField source="name" />
            <SelectField source="status" />
            <NumberField source="id" />
            <ReferenceField source="category" reference="category" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <ReferenceArrayField source="tags" reference="Tag" allowEmpty>
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
            </ReferenceArrayField>
            <EditButton />
        </Datagrid>
    </List>
)

export const PetShow = props => (
    <Show {...props} title="pet Show">
        <SimpleShowLayout>
            <TextField source="name" />
            <SelectField source="status" />
            <NumberField source="id" />
            <ReferenceField source="category" reference="category" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <ReferenceArrayField source="tags" reference="Tag" allowEmpty>
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
            </ReferenceArrayField>
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const PetCreate = props => (
    <Create {...props} title="Create pet">
        <SimpleForm validate={validationCreatepet}>
            <TextInput source="name" />
            <ReferenceInput source="category" reference="category" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <SelectInput source="status" choices={createchoicestatus} />
            <ReferenceArrayInput source="tags" reference="Tag" allowEmpty>
                <SelectArrayInput optionText="id" />
            </ReferenceArrayInput>
        </SimpleForm>
    </Create>
)

export const PetEdit = props => (
    <Edit {...props} title="Edit pet">
        <SimpleForm validate={validationEditpet}>
            <TextInput source="name" />
            <ReferenceInput source="category" reference="category" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <SelectInput source="status" choices={editchoicestatus} />
            <ReferenceArrayInput source="tags" reference="Tag" allowEmpty>
                <SelectArrayInput optionText="id" />
            </ReferenceArrayInput>
        </SimpleForm>
    </Edit>
)

