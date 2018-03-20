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
    DateInput,
    SelectField,
    SelectInput,
    BooleanField,
    BooleanInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateorder = values => {
    const errors = {};
    if (!values.quantity) {
        errors.quantity = ["quantity is required"];
    }
    if (!values.petId) {
        errors.petId = ["petId is required"];
    }
    return errors;
}

const validationEditorder = values => {
    const errors = {};
    return errors;
}

const editchoicestatus = [
    { id: 'placed', name: 'placed' },
    { id: 'approved', name: 'approved' },
    { id: 'delivered', name: 'delivered' },
];

export const OrderList = props => (
    <List {...props} title="order List">
        <Datagrid>
            <DateField source="shipDate" />
            <SelectField source="status" />
            <BooleanField source="complete" />
            <NumberField source="id" />
            <NumberField source="quantity" />
            <NumberField source="petId" />
            <EditButton />
        </Datagrid>
    </List>
)

export const OrderShow = props => (
    <Show {...props} title="order Show">
        <SimpleShowLayout>
            <DateField source="shipDate" />
            <SelectField source="status" />
            <BooleanField source="complete" />
            <NumberField source="id" />
            <NumberField source="quantity" />
            <NumberField source="petId" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const OrderCreate = props => (
    <Create {...props} title="Create order">
        <SimpleForm validate={validationCreateorder}>
            <NumberInput source="quantity" />
            <NumberInput source="petId" />
        </SimpleForm>
    </Create>
)

export const OrderEdit = props => (
    <Edit {...props} title="Edit order">
        <SimpleForm validate={validationEditorder}>
            <BooleanInput source="complete" />
            <DateInput source="shipDate" />
            <SelectInput source="status" choices={editchoicestatus} />
            <NumberInput source="petId" />
            <NumberInput source="quantity" />
        </SimpleForm>
    </Edit>
)

