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
    TextField,
    DateField,
    BooleanField,
} from 'admin-on-rest';

export const OrderList = props => (
    <List {...props} title={"Order List"}>
        <DataGrid>
            <NumberField source="id" />
            <TextField source="status" />
            <DateField source="shipDate" />
            <NumberField source="quantity" />
            <NumberField source="petId" />
            <BooleanField source="complete" />
        </DataGrid>
    </List>
)

export const OrderShow = props => (
    <Show {...props} title={"Order Show"}>
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="status" />
            <DateField source="shipDate" />
            <NumberField source="quantity" />
            <NumberField source="petId" />
            <BooleanField source="complete" />
        </SimpleShowLayout>
    </Show>
)

