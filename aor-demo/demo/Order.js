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
    BooleanField,
    BooleanInput,
    DateField,
    DateInput,
    SelectField,
    SelectInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateOrder = values => {
    const errors = {};
    if (!values.quantity) {
        errors.quantity = ["quantity is required"];
    }
    if (!values.petId) {
        errors.petId = ["petId is required"];
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
            <NumberField source="quantity" />
            <BooleanField source="complete" />
            <NumberField source="petId" />
            <DateField source="shipDate" />
            <NumberField source="id" />
            <SelectField source="status" />
            <EditButton />
        </DataGrid>
    </List>
)

export const OrderShow = props => (
    <Show {...props} title={"Order Show"}>
        <SimpleShowLayout>
            <NumberField source="quantity" />
            <BooleanField source="complete" />
            <NumberField source="petId" />
            <DateField source="shipDate" />
            <NumberField source="id" />
            <SelectField source="status" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const OrderCreate = props => (
    <Create {...props} title={"Create Order"}>
        <SimpleForm validate={validationCreateOrder}>
            <NumberInput source="quantity" />
            <NumberInput source="petId" />
        </SimpleForm>
    </Create>
)

export const OrderEdit = props => (
    <Edit {...props} title={"Edit Order"}>
        <SimpleForm validate={validationEditOrder}>
            <NumberInput source="quantity" />
            <BooleanInput source="complete" />
            <NumberInput source="petId" />
            <DateInput source="shipDate" />
            <SelectInput source="status" choices={editchoicestatus} />
        </SimpleForm>
    </Edit>
)

