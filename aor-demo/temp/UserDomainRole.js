/**
 * Generated UserDomainRole.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    ReferenceField,
    TextField,
    NumberField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    Show,
    SimpleShowLayout,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    UserDomainRoleFilter
} from './Filters';

const validationCreateUserDomainRole = values => {
    const errors = {};
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    return errors;
}

export const UserDomainRoleList = props => (
    <List {...props} title="UserDomainRole List" filters={<UserDomainRoleFilter />}>
        <Datagrid>
            <ReferenceField label="User" source="user_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <ReferenceField label="Domain" source="domain_id" reference="domains" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const UserDomainRoleCreate = props => (
    <Create {...props} title="UserDomainRole Create">
        <SimpleForm validate={validationCreateUserDomainRole}>
            <ReferenceInput label="User" source="user_id" reference="users" allowEmpty>
                <SelectInput source="id" optionText="username" />
            </ReferenceInput>
            <ReferenceInput label="Domain" source="domain_id" reference="domains" allowEmpty>
                <SelectInput source="id" optionText="name" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" optionText="label" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
)

export const UserDomainRoleShow = props => (
    <Show {...props} title="UserDomainRole Show">
        <SimpleShowLayout>
            <ReferenceField label="User" source="user_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <ReferenceField label="Domain" source="domain_id" reference="domains" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

/** End of Generated Code **/