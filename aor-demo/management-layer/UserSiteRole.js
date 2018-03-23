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
    TextField,
    TextInput,
    NumberInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateUserSiteRole = values => {
    const errors = {};
    if (!values.user_id) {
        errors.user_id = ["user_id is required"];
    }
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    return errors;
}

export const UserSiteRoleShow = props => (
    <Show {...props} title="UserSiteRole Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <ReferenceField label="User" source="user_id" reference="users" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <ReferenceField label="Site" source="site_id" reference="sites" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
)

export const UserSiteRoleCreate = props => (
    <Create {...props} title="UserSiteRole Create">
        <SimpleForm validate={validationCreateUserSiteRole}>
            <ReferenceInput label="User" source="user_id" reference="users" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="Site" source="site_id" reference="sites" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
)

export const UserSiteRoleList = props => (
    <List {...props} title="UserSiteRole List">
        <Datagrid>
            <DateField source="updated_at" />
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <ReferenceField label="User" source="user_id" reference="users" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <ReferenceField label="Site" source="site_id" reference="sites" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="created_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

