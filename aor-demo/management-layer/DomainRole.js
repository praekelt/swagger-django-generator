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
    NumberField,
    BooleanField,
    BooleanInput,
    NumberInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
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
            <DateField source="updated_at" />
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <ReferenceField label="Domain" source="domain_id" reference="domains" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="created_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const DomainRoleCreate = props => (
    <Create {...props} title="DomainRole Create">
        <SimpleForm validate={validationCreateDomainRole}>
            <BooleanInput source="grant_implicitly" />
            <ReferenceInput label="Domain" source="domain_id" reference="domains" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
)

export const DomainRoleShow = props => (
    <Show {...props} title="DomainRole Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <ReferenceField label="Domain" source="domain_id" reference="domains" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
)

export const DomainRoleEdit = props => (
    <Edit {...props} title="DomainRole Edit">
        <SimpleForm validate={validationCreateDomainRole}>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Edit>
)

