import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    BooleanField,
    BooleanInput,
    NumberField,
    NumberInput,
    SelectField,
    SelectInput,
    DateField,
    DateInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateOrder = values => {
    const errors = {};
    if (!values.petId) {
        errors.petId = ["petId is required"];
    }
    if (!values.quantity) {
        errors.quantity = ["quantity is required"];
    }
    return errors;
}

const validationEditOrder = values => {
    const errors = {};
    return errors;
}

const editchoicestatus = [
    { id: 'placed', name: 'placed' },
    { id: 'approved', name: 'approved' },
    { id: 'delivered', name: 'delivered' },
];

export const OrderList = props => (
    <List {...props} title={"Order List"}>
        <DataGrid>
            <BooleanField source="complete" />
            <NumberField source="id" />
            <SelectField source="status" />
            <NumberField source="petId" />
            <NumberField source="quantity" />
            <DateField source="shipDate" />
            <EditButton />
        </DataGrid>
    </List>
)

export const OrderShow = props => (
    <Show {...props} title={"Order Show"}>
        <SimpleShowLayout>
            <BooleanField source="complete" />
            <NumberField source="id" />
            <SelectField source="status" />
            <NumberField source="petId" />
            <NumberField source="quantity" />
            <DateField source="shipDate" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const OrderCreate = props => (
    <Create {...props} title={"Create Order"}>
        <SimpleForm validate={validationCreateOrder}>
            <NumberInput source="petId" />
            <NumberInput source="quantity" />
        </SimpleForm>
    </Create>
)

export const OrderEdit = props => (
    <Edit {...props} title={"Edit Order"}>
        <SimpleForm validate={validationEditOrder}>
            <NumberInput source="petId" />
            <NumberInput source="quantity" />
            <BooleanInput source="complete" />
            <DateInput source="shipDate" />
            <SelectInput source="status" choices={editchoicestatus} />
        </SimpleForm>
    </Edit>
)

