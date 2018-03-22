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
    NumberInput,
    DateField,
    DateInput,
    BooleanField,
    BooleanInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateDomainRole = values => {
    const errors = {};
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    return errors;
}

const validationEditDomainRole = values => {
    const errors = {};
    return errors;
}

export const DomainRoleList = props => (
    <List {...props} title="DomainRole List">
        <Datagrid>
            <NumberField source="domain_id" />
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const DomainRoleShow = props => (
    <Show {...props} title="DomainRole Show">
        <SimpleShowLayout>
            <NumberField source="domain_id" />
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const DomainRoleCreate = props => (
    <Create {...props} title="Create DomainRole">
        <SimpleForm validate={validationCreateDomainRole}>
            <NumberInput source="domain_id" />
            <NumberInput source="role_id" />
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Create>
)

export const DomainRoleEdit = props => (
    <Edit {...props} title="Edit DomainRole">
        <SimpleForm validate={validationEditDomainRole}>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Edit>
)

