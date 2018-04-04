/**
 * Generated Domain.js code. Edit at own risk.
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
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    DomainFilter
} from './Filters';

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

export const DomainList = props => (
    <List {...props} title="Domain List" filters={<DomainFilter />}>
        <Datagrid>
            <NumberField source="id" />
            <ReferenceField label="Domain" source="parent_id" reference="domains" linkType="show" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <TextField source="name" />
            <TextField source="description" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const DomainCreate = props => (
    <Create {...props} title="Domain Create">
        <SimpleForm validate={validationCreateDomain}>
            <ReferenceInput label="Domain" source="parent_id" reference="domains" allowEmpty>
                <SelectInput source="id" optionText="" />
            </ReferenceInput>
            <TextInput source="name" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const DomainShow = props => (
    <Show {...props} title="Domain Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField label="Domain" source="parent_id" reference="domains" linkType="show" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <TextField source="name" />
            <TextField source="description" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const DomainEdit = props => (
    <Edit {...props} title="Domain Edit">
        <SimpleForm validate={validationEditDomain}>
            <ReferenceInput label="Domain" source="parent_id" reference="domains" allowEmpty>
                <SelectInput source="id" optionText="" />
            </ReferenceInput>
            <TextInput source="name" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/