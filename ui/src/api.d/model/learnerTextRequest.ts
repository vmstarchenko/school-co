/**
 * 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { LearnerTextGenreRequest } from './learnerTextGenreRequest';


export interface LearnerTextRequest { 
    text: string;
    status: LearnerTextRequest.StatusEnum;
    genre: LearnerTextGenreRequest;
}
export namespace LearnerTextRequest {
    export type StatusEnum = 1 | 10;
    export const StatusEnum = {
        NUMBER_1: 1 as StatusEnum,
        NUMBER_10: 10 as StatusEnum
    };
}

