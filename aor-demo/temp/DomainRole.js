/**
 * Generated DomainRole.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    ReferenceField,
    NumberField,
    BooleanField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    BooleanInput,
    Show,
    SimpleShowLayout,
    Edit,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    DomainRoleFilter
} from './Filters';

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
    <List {...props} title="DomainRole List" filters={<DomainRoleFilter />}>
        <Datagrid>
            <ReferenceField label="Domain" source="domain_id" reference="domains" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const DomainRoleCreate = props => (
    <Create {...props} title="DomainRole Create">
        <SimpleForm validate={validationCreateDomainRole}>
            <ReferenceInput label="Domain" source="domain_id" reference="domains" allowEmpty>
                <SelectInput source="id" optionText="name" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" optionText="label" />
            </ReferenceInput>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Create>
)

export const DomainRoleShow = props => (
    <Show {...props} title="DomainRole Show">
        <SimpleShowLayout>
            <ReferenceField label="Domain" source="domain_id" reference="domains" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const DomainRoleEdit = props => (
    <Edit {...props} title="DomainRole Edit">
        <SimpleForm validate={validationEditDomainRole}>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/